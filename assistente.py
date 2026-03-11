import os
import whisper
import sounddevice as sd
from scipy.io.wavfile import write
from google import genai
from google.genai import types
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv()
 
client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

# Configurações iniciais
LANGUAGE = 'pt'
AUDIO_FILE = 'request_audio.wav'
RESPONSE_FILE = 'response_audio.wav'

def record_audio(filename, duration=5, fs=44100):
    print(f"🎤 Ouvindo por {duration} segundos... (Fale agora!)")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait() 
    write(filename, fs, recording) 
    return filename

try:
    # 1. Gravar Áudio
    record_audio(AUDIO_FILE, duration=6)
    
    # 2. Transcrever com Whisper
    print("⏳ Transcrevendo o áudio...")
    model_whisper = whisper.load_model("small")
    result = model_whisper.transcribe(AUDIO_FILE, fp16=False, language=LANGUAGE)
    transcription = result["text"]
    print(f"🗣️ Você disse: {transcription}")

    # 3. Enviar para o Gemini
    print("🧠 Pensando na resposta...")
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=transcription,
        config=types.GenerateContentConfig(
            system_instruction="Você é um assistente virtual carismático. Responda de forma concisa em no máximo 1 parágrafo."
        )
    )
    
    gemini_response = response.text
    print(f"🤖 Gemini respondeu: {gemini_response}")

    # 4. Transformar Texto em Áudio e Tocar 
    print("🔊 Gerando e reproduzindo áudio de resposta...")
    gtts_object = gTTS(text=gemini_response, lang=LANGUAGE, slow=False)
    gtts_object.save(RESPONSE_FILE)

    # Toca o áudio nativamente no Windows
    os.startfile(RESPONSE_FILE)

except Exception as e:
    print(f"❌ Ops! Ocorreu um erro: {e}")
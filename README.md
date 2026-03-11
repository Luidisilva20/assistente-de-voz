# 🎙️ Assistente Virtual Inteligente (Voice-to-Voice)

Este projeto é um assistente virtual operado 100% por voz, desenvolvido em Python. Ele é capaz de ouvir o usuário pelo microfone, transcrever o áudio usando Inteligência Artificial, gerar uma resposta inteligente e reproduzir essa resposta em áudio de volta para o usuário.

## 🚀 Como funciona?

O fluxo do assistente é dividido em 4 etapas:
1. **Captura de Áudio:** Grava a voz do usuário via microfone nativo.
2. **Transcrição (Speech-to-Text):** Utiliza o modelo **Whisper** (da OpenAI) executado localmente para converter o áudio em texto.
3. **Processamento Cognitivo:** Envia o texto para a API do **Google Gemini** (modelo `gemini-2.5-flash`), que atua como o "cérebro" do assistente, gerando respostas rápidas e carismáticas.
4. **Síntese de Voz (Text-to-Speech):** Utiliza o **gTTS** (Google Text-to-Speech) para transformar a resposta de texto do Gemini em áudio e reproduzi-lo no sistema.

## 🛠️ Tecnologias Utilizadas

* **Python 3.13**
* **OpenAI Whisper:** Transcrição de áudio de alta precisão.
* **Google GenAI (API do Gemini):** Geração de linguagem natural.
* **gTTS:** Geração de voz.
* **Sounddevice & SciPy:** Manipulação de áudio local.
* **FFmpeg:** Processamento de mídia.

## ⚙️ Pré-requisitos

Para rodar este projeto na sua máquina, você precisará ter instalado:
* Python 3.8 ou superior.
* [FFmpeg](https://ffmpeg.org/) (necessário para o Whisper funcionar corretamente).
* Uma chave de API gratuita do [Google AI Studio](https://aistudio.google.com/).

## 💻 Como executar o projeto localmente

**1. Clone o repositório:**
```bash
git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)
cd NOME-DO-REPOSITORIO
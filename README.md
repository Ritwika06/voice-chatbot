# Voice Chatbot

This repository contains a voice-enabled chatbot that integrates ASR (Automatic Speech Recognition), LLM (Large Language Model), and TTS (Text-to-Speech) components. The chatbot allows users to have real-time voice interactions.

## Features

- **Speech-to-Text (ASR)**: Accurately transcribes user speech into text using **Whisper**, ensuring high-quality voice recognition.

- **Conversational AI (LLM)**: Processes transcribed text and generates intelligent responses using **Mistral from Ollama**, enhancing natural conversation.

- **Text-to-Speech (TTS)**: Converts generated responses into natural-sounding speech using **gTTS**, providing a seamless voice interaction experience.

- **Device-Specific Audio Configuration**: Allows users to select the correct microphone and speaker for proper functioning.

## Installation

### 1. Clone the Repository

```sh
git clone https://github.com/Ritwika06/voice-chatbot.git
cd voice-chatbot
```

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

---

## Usage

### 1. Select the Correct Audio Input Device

The chatbot requires the correct microphone device to record your voice input. You can list available audio devices using:

```sh
python -m sounddevice
```

Identify your microphone device from the list and update `config.py`:

```python
device_index = 1  # Replace with your microphone device index
```

Alternatively, you can modify the `record_audio` function to accept the `device_index` as an argument.

### 2. Run the Chatbot

To start the chatbot, run:

```sh
streamlit run app.py --server.fileWatcherType none
```

Speak into the microphone, and the chatbot will respond with voice output.

---

## Troubleshooting

### **PortAudio Error: Error Querying Device**

If you see an error like:

```sh
sounddevice.PortAudioError: Error querying device
```

Try changing the `device_index` in `config.py` to match your microphone from `python -m sounddevice`.




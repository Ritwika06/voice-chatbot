import streamlit as st
import os
from utils.record_audio import record_audio
from utils.transcribe_whisper import transcribe_audio
from utils.get_llm_response import get_mistral_llm_response
from utils.get_tts_response import generate_speech

# Configuration
duration = 5
fs = 48000
device_index = 1
audio_file_path = 'audio/question.wav'
tts_audio_file_path = 'audio/answer.wav'

# Streamlit UI Elements
st.markdown(
    "<h1 style='text-align: center; color: #FF5733;'>🎙️ Voice Chatbot</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    "<p style='text-align: center; font-size: 18px; color: #555;'>"
    "Ask a question, get an AI response, and hear it spoken back!</p>",
    unsafe_allow_html=True,
)

st.divider()  # Adds a visual divider

# UI placeholders
status_placeholder = st.empty()
transcription_placeholder = st.empty()
response_placeholder = st.empty()
tts_placeholder = st.empty()

# Session state initialization
if "process_running" not in st.session_state:
    st.session_state.process_running = False

if "transcription_text" not in st.session_state:
    st.session_state.transcription_text = ""

if "llm_response" not in st.session_state:
    st.session_state.llm_response = ""

# Ask Question Button with Styling
st.markdown(
    """
    <style>
        div.stButton > button:first-child {
            background-color: #FF5733;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 10px;
            width: 100%;
        }
        div.stButton > button:first-child:hover {
            background-color: #E74C3C;
        }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("🎤 Ask a Question", disabled=st.session_state.process_running):
    st.session_state.process_running = True

    with st.spinner("🎙️ Recording... Please wait."):
        record_audio(filepath=audio_file_path, duration=duration, fs=fs, device_index=device_index)
    status_placeholder.success("✅ Recording complete!")

    if os.path.exists(audio_file_path):
        with st.spinner("📝 Transcribing..."):
            st.session_state.transcription_text = transcribe_audio(audio_file_path)

        transcription_placeholder.markdown(
            f"""
            <div style="background-color:#2841bf;padding:15px; border-radius:10px; margin: 10px 0;">
                <strong style="color:#154360;">🗣️ You:</strong> {st.session_state.transcription_text}
            </div>
            """,
            unsafe_allow_html=True,
        )

# Get LLM response
if st.session_state.transcription_text:
    with st.spinner("🤖 Thinking... Please wait."):
        st.session_state.llm_response = get_mistral_llm_response(st.session_state.transcription_text)

    response_placeholder.markdown(
        f"""
        <div style="background-color:#876723;padding:15px; border-radius:10px; margin:10px 0;">
            <strong style="color:#7B241C;">🤖 AI:</strong> {st.session_state.llm_response}
        </div>
        """,
        unsafe_allow_html=True,
    )

# Convert text response to speech
if st.session_state.llm_response:
    with st.spinner("🔊 Converting response to speech... Please wait."):
        generate_speech(st.session_state.llm_response, tts_audio_file_path)

    tts_placeholder.success("✅ LLM response converted to speech!")
    st.audio(tts_audio_file_path, format="audio/mp3", autoplay=True)

# Reset process state
st.session_state.process_running = False

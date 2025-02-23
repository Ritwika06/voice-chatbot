from gtts import gTTS

def generate_speech(text_input,output):
    mp3 = gTTS(text=f"{text_input}", lang= 'en')
    mp3.save(output)
    

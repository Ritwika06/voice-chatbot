import sounddevice as sd
import soundfile as sf

print(sd.query_devices())

def record_audio(filepath, duration, fs, device_index):
    print("Recording...")
    audio_data = sd.rec(int(duration*fs), samplerate=fs,channels=1,device=device_index,dtype='float32')
    sd.wait()
    sf.write(filepath,audio_data,fs)
    print(f"Recording saved successfully at {filepath}")
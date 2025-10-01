import wave
import struct
import math

def generate_beep(filename, freq=440, duration=0.2, volume=0.5, samplerate=44100):
    n_samples = int(samplerate * duration)
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)       # mono
        wav_file.setsampwidth(2)       # 16-bit
        wav_file.setframerate(samplerate)

        for i in range(n_samples):
            sample = volume * math.sin(2 * math.pi * freq * (i / samplerate))
            wav_file.writeframes(struct.pack('<h', int(sample * 32767)))

# Luo kaksi piippausta
generate_beep("eat.wav", freq=800, duration=0.1)     # kirkas lyhyt piippaus
generate_beep("gameover.wav", freq=400, duration=0.6)  # matala pidempi piippaus

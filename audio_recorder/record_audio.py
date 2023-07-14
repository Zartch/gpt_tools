import soundcard as sc
import numpy as np
import soundfile as sf
import sys
import threading

def grabar_audio_micrófono(duracion, archivo_salida):
    mic = sc.default_microphone()
    fs = 44100
    with mic.recorder(samplerate=fs, channels=1) as recorder:
        print("Grabando audio del micrófono...")
        audio_data = recorder.record(numframes=int(duracion * fs))
        print("Grabación del micrófono terminada.")
        sf.write(archivo_salida, audio_data, fs, format='wav')

def grabar_audio_sistema(duracion, archivo_salida):
    loopback = sc.default_speaker().loopback()
    fs = 44100
    with loopback.recorder(samplerate=fs, channels=1) as recorder:
        print("Grabando audio del sistema...")
        audio_data = recorder.record(numframes=int(duracion * fs))
        print("Grabación del sistema terminada.")
        sf.write(archivo_salida, audio_data, fs, format='wav')

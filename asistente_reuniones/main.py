
from  utils.audio_capture import AudioCapture


def audio_received(data):
    print("Audio recibido")


if name == 'main':
    import time

audio_capture = AudioCapture(callback=audio_received)

print("Iniciando grabación...")
audio_capture.start()

time.sleep(5)

print("Deteniendo grabación...")
audio_capture.stop()

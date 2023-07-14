import threading
from record_audio import grabar_audio_micrófono, grabar_audio_sistema

if __name__ == "__main__":
    duracion = 5  # Duración en segundos
    archivo_salida_microfono = "grabacion_microfono.wav"
    archivo_salida_sistema = "grabacion_sistema.wav"

    mic_thread = threading.Thread(target=grabar_audio_micrófono, args=(duracion, archivo_salida_microfono))
    sistema_thread = threading.Thread(target=grabar_audio_sistema, args=(duracion, archivo_salida_sistema))

    mic_thread.start()
    sistema_thread.start()

    mic_thread.join()
    sistema_thread.join()

    print("Grabaciones completadas.")
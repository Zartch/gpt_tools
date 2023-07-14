# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#

from asistente_reuniones.utils.audio_capture import AudioCapture
from audio.process_chunk import process_speaker_segments

if __name__ == '__main__':
    # import time
    #
    # def audio_received(data):
    #     print("Audio recibido")
    #
    # audio_capture = AudioCapture(callback=audio_received, output_filename="grabacion.wav")
    #
    # print("Iniciando grabación...")
    # audio_capture.start()
    #
    # time.sleep(5)
    #
    # print("Deteniendo grabación...")
    # audio_capture.stop()
    # print("Finalizado.")
    print("START...")
    process_speaker_segments('/home/smorales/Documentos/personal/FS/Audios_partida/chunks/test/20230707_chunk1_diarization.txt',
                             '/home/smorales/Documentos/personal/FS/Audios_partida/chunks/test/20230707_chunk1.mp3',
                             '/home/smorales/Documentos/personal/FS/Audios_partida/chunks/test/audios_splitted')

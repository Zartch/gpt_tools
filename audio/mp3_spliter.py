from pydub import AudioSegment
import os


def split_audio_chunks(file_path, duration_s, output_folder):
    # Load audio file
    audio = AudioSegment.from_mp3(file_path)

    # Duration in milliseconds
    duration_ms = duration_s * 1000

    # Start and end times
    start_time = 0
    end_time = duration_ms

    # Current chunk counter
    chunk_counter = 1

    # Length of audio file
    audio_length = len(audio)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over audio file
    while start_time < audio_length:
        # Create audio chunk
        chunk = audio[start_time:end_time]

        # Filename for the chunk
        chunk_filename = os.path.join(output_folder, f'20230707_chunk{chunk_counter}.mp3')

        # Export chunk as .mp3
        chunk.export(chunk_filename, format="mp3")

        # Update start and end times
        start_time = end_time
        end_time = end_time + duration_ms

        # Increment chunk counter
        chunk_counter += 1


# split_audio_chunks('/home/smorales/Documentos/personal/FS/Audios_partida/Partida_20230707.mp3', 60 * 21,
#             '/home/smorales/Documentos/personal/FS/Audios_partida/chunks')




def split_audio(file_path, start_time, end_time, output_folder, speaker = None):
    """
    Divide un archivo de audio en un rango de tiempo especificado.

    :param file_path: La ruta del archivo de audio a dividir.
    :param start_time: El tiempo de inicio del segmento a extraer, en milisegundos.
    :param end_time: El tiempo de final del segmento a extraer, en milisegundos.
    :param output_folder: El directorio donde guardar el archivo de audio generado.
    """
    audio = AudioSegment.from_mp3(file_path)

    # Recuerda que PyDub trabaja en milisegundos
    start_time_ms = start_time
    end_time_ms = end_time

    # Extraer el segmento de audio
    audio_segment = audio[start_time_ms:end_time_ms]

    # Crear la ruta del archivo de salida
    output_file_path = os.path.join(output_folder, f"output_{start_time_ms}_{end_time_ms}_{speaker}.mp3")

    # Guardar el segmento de audio en un archivo
    audio_segment.export(output_file_path, format="mp3")
    print(f"Audio segment exported: {output_file_path}")
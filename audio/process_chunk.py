from audio.mp3_spliter import split_audio
import re

def convert_time_str_to_milliseconds(time_str):
    """
    Convierte una cadena de tiempo en formato HH:MM:SS.sss a milisegundos.

    :param time_str: La cadena de tiempo a convertir.
    :return: El tiempo en milisegundos.
    """
    hours, minutes, seconds = map(float, time_str.split(':'))
    return int((hours * 3600 + minutes * 60 + seconds) * 1000)



def process_speaker_segments(segment_file_path, audio_file_path, output_folder):
    """
    Procesa un archivo de segmentos de hablante, dividiendo el archivo de audio correspondiente en trozos.

    :param segment_file_path: La ruta del archivo de segmentos de hablante.
    :param audio_file_path: La ruta del archivo de audio a dividir.
    :param output_folder: El directorio donde guardar los archivos de audio generados.
    """
    # Expresión regular para parsear las líneas del archivo de segmentos
    regex = re.compile(r"\[\s*(\d{2}:\d{2}:\d{2}\.\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}\.\d{3})\]\s*\w+\s*(SPEAKER_\d{2})")

    with open(segment_file_path, 'r') as f:
        for line in f:
            match = regex.match(line)
            if match:
                start_time_str, end_time_str, speaker = match.groups()

                # Convertir los tiempos de inicio y final a milisegundos
                start_time = convert_time_str_to_milliseconds(start_time_str)
                end_time = convert_time_str_to_milliseconds(end_time_str)

                # Dividir el archivo de audio
                split_audio(audio_file_path, start_time, end_time, output_folder, speaker)

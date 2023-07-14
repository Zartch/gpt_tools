import os
import openai

openai.api_key = "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"



import os
import openai
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def transcribe_audio_chunks(input_folder, model="whisper-1", language="es", response_format="text"):
    logging.info(f'Starting transcription process in folder {input_folder}...')

    try:
        # Iterar sobre cada archivo en el directorio de entrada
        for filename in os.listdir(input_folder):
            if filename.endswith('.mp3'):
                file_path = os.path.join(input_folder, filename)
                logging.info(f'Transcribing file {filename}...')

                # Transcribir el archivo
                with open(file_path, "rb") as audio_file:
                    transcript = openai.Audio.transcribe(
                        file=audio_file,
                        model=model,
                        response_format=response_format,
                        language=language
                    )

                # Crear el nombre del archivo de la transcripción
                transcript_filename = os.path.splitext(filename)[0] + '.txt'

                # Escribir la transcripción en un archivo de texto
                with open(os.path.join(input_folder, transcript_filename), 'w') as transcript_file:
                    transcript_file.write(str(transcript))
                    logging.info(f'Transcription saved as {transcript_filename}')
    except Exception as e:
        print(e)

    logging.info(f'Transcription process completed for folder {input_folder}.')

# Llama a la función con la ruta del directorio que contiene tus chunks de audio
transcribe_audio_chunks('/home/smorales/Documentos/personal/FS/Audios_partida/chunks/test')

from pyannote.audio import Pipeline

token = "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"

pipeline = Pipeline.from_pretrained('pyannote/speaker-diarization@2.1', use_auth_token="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")
DEMO_FILE = {'uri': 'blabal', 'audio': '/home/smorales/Documentos/personal/FS/Audios_partida/chunks/test/20230707_chunk1.mp3'}
dz = pipeline(DEMO_FILE, min_speakers=2, max_speakers=5)

with open("diarization.txt", "w") as text_file:
    text_file.write(str(dz))




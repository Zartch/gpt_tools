import wave
import threading
from pulsectl import Pulse

PA_SAMPLE_S16LE = 3

class AudioCapture:
    def __init__(self, callback, rate=44100, chunk_size=1024, channels=1, format=PA_SAMPLE_S16LE, output_filename=None):
        self.callback = callback
        self.rate = rate
        self.chunk_size = chunk_size
        self.channels = channels
        self.format = format
        self.output_filename = output_filename

        self.is_recording = False
        self.wavefile = None
        self.thread = None

    def _record(self):
        with Pulse('record') as pulse:
            sinks = pulse.sink_list()
            monitor_source = None
            for sink in sinks:
                if sink.description.startswith("Null Output"):
                    monitor_source = sink.monitor_source
                    break

            if monitor_source is None:
                print("No se encontró la fuente de monitor. Asegúrese de que module-null-sink esté cargado en PulseAudio.")
                return

            for source_output in pulse.source_output_list():
                if source_output.source == monitor_source:
                    pulse.source_output_mute(source_output.index, mute=False)

            stream = pulse.stream_connect_record(monitor_source, rate=self.rate, channels=self.channels, format=self.format)

            while self.is_recording:
                data = pulse.stream_read(stream, nbytes=self.chunk_size * self.channels * 2)
                self.callback(data)

    def start(self):
        if self.is_recording:
            print("Ya se está grabando audio.")
            return

        self.is_recording = True
        self.thread = threading.Thread(target=self._record)
        self.thread.start()

        if self.output_filename:
            self.wavefile = wave.open(self.output_filename, 'wb')
            self.wavefile.setnchannels(self.channels)
            self.wavefile.setsampwidth(2)  # pulse.PA_SAMPLE_S16LE tiene una longitud de muestra de 2 bytes
            self.wavefile.setframerate(self.rate)

        print("La grabación de audio ha comenzado.")

    def stop(self):
        if not self.is_recording:
            print("La grabación ya está detenida.")
            return

        self.is_recording = False
        if self.thread is not None:
            self.thread.join()

        if self.wavefile:
            self.wavefile.close()
            self.wavefile = None

        print("La grabación de audio se ha detenido.")

    def process_audio_chunk(self, in_data):
        if self.is_recording:
            if self.wavefile:
                self.wavefile.writeframes(in_data)
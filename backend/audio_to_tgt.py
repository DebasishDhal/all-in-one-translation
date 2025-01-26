import whisper
import numpy as np
from pydub import AudioSegment
from deep_translator import GoogleTranslator

def audio_to_numpy(audio_file_input):
    audio = AudioSegment.from_file(audio_file_input)
    audio = audio.set_channels(1).set_frame_rate(16000)
    samples = np.array(audio.get_array_of_samples(), dtype=np.float32)

    return samples / np.iinfo(audio.array_type).max

def src_audio_to_eng_translator(audio_file_input):
    audio_data = audio_to_numpy(audio_file_input)

    model = whisper.load_model("turbo")
    result = model.transcribe(audio_data)

    translated_text = GoogleTranslator(source='auto', target='en').translate(result["text"])
    return translated_text
    # return result['text']
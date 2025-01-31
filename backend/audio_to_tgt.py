import whisper
import numpy as np
from pydub import AudioSegment
from deep_translator import GoogleTranslator

def audio_to_numpy(audio_file_input):
    audio = AudioSegment.from_file(audio_file_input)
    audio = audio.set_channels(1).set_frame_rate(16000)
    samples = np.array(audio.get_array_of_samples(), dtype=np.float32)

    return samples / np.iinfo(audio.array_type).max

def src_audio_to_eng_translator(audio_file_input, model_size = "turbo"):
    audio_data = audio_to_numpy(audio_file_input)

    model = whisper.load_model(model_size)
    result = model.transcribe(audio_data)
    input_text = result["text"]
    language = result["language"]
    translated_text = GoogleTranslator(source='auto', target='en').translate(input_text)
    return input_text, translated_text, language
    # return result['text']
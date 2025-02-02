import whisper
import numpy as np
from pydub import AudioSegment
from deep_translator import GoogleTranslator, detection
import os

available_languages = GoogleTranslator().get_supported_languages(as_dict=True)
formatted_languages = {key.title(): value for key, value in available_languages.items()}
formatted_codes = {value: key.title() for key, value in available_languages.items()}

lang_detect_key = os.getenv("detect_language_api_key")

def audio_to_numpy(audio_file_input):
    audio = AudioSegment.from_file(audio_file_input)
    audio = audio.set_channels(1).set_frame_rate(16000)
    samples = np.array(audio.get_array_of_samples(), dtype=np.float32)

    return samples / np.iinfo(audio.array_type).max

def src_audio_to_eng_translator(audio_file_input, model_size = "turbo", target_lang = "English"):
    audio_data = audio_to_numpy(audio_file_input)

    model = whisper.load_model(model_size)
    result = model.transcribe(audio_data)
    input_text = result["text"]

    src_lang_code = detection.single_detection(input_text, api_key = lang_detect_key)
    src_lang = formatted_codes.get(src_lang_code, 'Source language not detected')
    target_lang_code = formatted_languages.get(target_lang, 'en')
    translated_text = GoogleTranslator(source='auto', target=target_lang_code).translate(input_text)
    return input_text, translated_text, src_lang
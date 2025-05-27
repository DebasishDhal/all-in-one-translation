from deep_translator import GoogleTranslator, detection
from langdetect import detect
import os

available_languages = GoogleTranslator().get_supported_languages(as_dict=True)
formatted_languages = {key.title(): value for key, value in available_languages.items()}
formatted_codes = {value: key.title() for key, value in available_languages.items()}

lang_detect_key = os.getenv("detect_language_api_key")

def src_txt_to_eng_translator(input_text, target_lang = 'English'):
    target_lang_code = formatted_languages.get(target_lang, 'en')
    # src_lang_code = detection.single_detection(input_text, api_key = lang_detect_key)
    src_lang_code = detect(input_text)
    src_lang = formatted_codes.get(src_lang_code, 'Source language not detected')
    translated = GoogleTranslator(source='auto', target=target_lang_code).translate(input_text)
    return translated, src_lang
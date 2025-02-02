from deep_translator import GoogleTranslator

available_languages = GoogleTranslator().get_supported_languages(as_dict=True)
formatted_languages = {key.title(): value for key, value in available_languages.items()}

def src_txt_to_eng_translator(input_text, target_lang = 'English'):
    target_lang_code = formatted_languages.get(target_lang, 'en')
    translated = GoogleTranslator(source='auto', target=target_lang_code).translate(input_text)
    return translated
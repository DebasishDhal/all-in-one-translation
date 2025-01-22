from deep_translator import GoogleTranslator

def src_txt_to_eng_translator(input_text):
    translated = GoogleTranslator(source='auto', target='en').translate(input)
    return translated
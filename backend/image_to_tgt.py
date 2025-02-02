# from PIL import Image

# def src_image_to_eng_translator(image_input_file):
#     return "Random"
from deep_translator import GoogleTranslator
import pytesseract

available_languages = GoogleTranslator().get_supported_languages(as_dict=True)
formatted_languages = {key.title(): value for key, value in available_languages.items()}
formatted_codes = {value: key.title() for key, value in available_languages.items()}

pytesseract_language_dict = {'English': 'eng', 'French': 'fra', 'Odia': 'ori', 'Hindi': 'hin',
                 'Bengali': 'ben', 'Telugu': 'tel', 'Hindi': 'hin', 'Malayalam': 'mal',
                 'Kannada': 'kan', 'Tamil': 'tam', 'Marathi': 'mar', 'Gujarati': 'guj', 
                 'Punjabi': 'pan', 'Sinhalese': 'sin',
                 'Arabic': 'ara', 'German': 'deu', 'Spanish': 'spa', 'Italian': 'ita',
                 'Russian': 'rus', 'Japanese': 'jpn', 'Korean': 'kor', 'Hebrew': 'heb',
                 'Persian': 'fas', 'Chinese Simplified': 'chi_sim', 'Chinese Traditional': 'chi_tra',
                 }

def src_image_to_eng_translator(input_image, image_lang = 'eng', target_lang = 'English'):
    image_text = pytesseract.image_to_string(input_image, lang = pytesseract_language_dict.get(image_lang, 'eng'))
    
    target_lang_code = formatted_languages.get(target_lang, 'en')
    translated = GoogleTranslator(source='auto', target=target_lang_code).translate(image_text)
    return image_text, translated
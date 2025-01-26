# from PIL import Image

# def src_image_to_eng_translator(image_input_file):
#     return "Random"
from deep_translator import GoogleTranslator
import pytesseract

language_dict = {'English': 'eng', 'French': 'fra', 'Odia': 'ori', 'Hindi': 'hin',
                 'Bengali': 'ben', 'Telugu': 'tel', 'Hindi': 'hin', 'Malayalam': 'mal',
                 'Kannada': 'kan', 'Tamil': 'tam', 'Marathi': 'mar', 'Gujarati': 'guj', 
                 'Punjabi': 'pan', 'Sinhalese': 'sin',
                 'Arabic': 'ara', 'German': 'deu', 'Spanish': 'spa', 'Italian': 'ita',
                 'Russian': 'rus', 'Japanese': 'jpn', 'Korean': 'kor', 'Hebrew': 'heb',
                 'Persian': 'fas', 'Chinese Simplified': 'chi_sim', 'Chinese Traditional': 'chi_tra',
                 }

def src_image_to_eng_translator(input_image, lang = 'eng'):
    image_text = pytesseract.image_to_string(input_image, lang = language_dict.get(lang, 'eng'))
    
    translated = GoogleTranslator(source='auto', target='en').translate(image_text)
    return image_text, translated
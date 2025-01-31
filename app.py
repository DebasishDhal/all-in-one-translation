import gradio as gr

from backend.text_to_tgt import src_txt_to_eng_translator
from backend.audio_to_tgt import src_audio_to_eng_translator
from backend.image_to_tgt import src_image_to_eng_translator, language_dict
# from backend.video_to_tgt import src_video_to_eng_translator

heading_txt = "Text-to-English"
description_txt = '''Enter text in any language, and get the translation in English.'''

txt_interface = gr.Interface(
    fn=src_txt_to_eng_translator,
    inputs=[
        gr.Textbox(label="Text Input"),
    ],
    outputs=gr.Textbox(label="Translation"),
    title=heading_txt,
    description=description_txt
)

heading_image = "Image-to-English"
description_image = "Upload an image to extract text and translate it to English."

sorted_languages = sorted(language_dict.keys())

image_interface = gr.Interface(
    fn=src_image_to_eng_translator,
    inputs=[
        gr.Image(label="Upload an Image", type="filepath"),  
        gr.Dropdown(choices=sorted_languages, 
                    label="Select Language", 
                    # default='English'
                   )
    ],  
    outputs=[
        gr.Textbox(label="Image Text"),
        gr.Textbox(label="Translated Text")
    ],
    title="Image Text Extractor and Translator",
    description=description_image,
)

heading_audio = "Audio-to-English"
description_audio = "Upload an audio file to extract text and translate it to English."

audio_interface = gr.Interface(
    fn=src_audio_to_eng_translator,
    inputs=[gr.Audio(label="Upload an Audio file", type="filepath"),
            gr.Dropdown(
            choices=["turbo", "base", "tiny", "small", "medium", "large"],
            label="Select Whisper Model size",
        )
            ],  
    outputs=[gr.Textbox(label="Original text"), 
             gr.Textbox(label="Translated text"),
             gr.Textbox(label="Original Language")],
    title=heading_audio,
    description=description_audio
)
combined_interface = gr.TabbedInterface(
    [txt_interface, image_interface, audio_interface],
    ['Text-to-English', 'Image-to-English', 'Audio-to-English']
)

combined_interface.launch()
import gradio as gr
from backend.text_to_tgt import src_txt_to_eng_translator, formatted_languages
from backend.audio_to_tgt import src_audio_to_eng_translator
from backend.image_to_tgt import src_image_to_eng_translator, language_dict
# from backend.video_to_tgt import src_video_to_eng_translator

heading_txt = "Text-to-English"
description_txt = '''Enter text in any language, and get the translation in English.'''

language_list = formatted_languages.keys()

txt_interface = gr.Interface(
    fn=src_txt_to_eng_translator,
    inputs=[
        gr.Textbox(label="Text Input"),
        gr.Dropdown(choices=language_list, label="Select Target Language, Default: English", value="English", interactive=True)
    ],
    outputs=gr.Textbox(label="Translation"),
    title=heading_txt,
    description=description_txt,
    examples=[
        ["Bonjour, comment ça va ?"],
        ["Привет, как дела?"],
        ["Hola, ¿cómo estás?"],
        ["你好，你怎么样？"],
        ["Guten Tag! Wie geht's dir?"]
    ]
)

heading_image = "Image-to-English"
description_image = "Upload an image to extract text and translate it to English. Make sure to choose language in 'Select Language'"

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
    examples=[
        ["examples/images/hindi_image_sample.jpg", "Hindi"],
        ["examples/images/odia_sample_image.png", "Odia"],
        ["examples/images/russian_sample_image.png", "Russian"]
    ]
)

heading_audio = "Audio-to-English"
description_audio = "Upload an audio file to extract text and translate it to English. Takes too much time without GPU."

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
    description=description_audio,
    examples=[
        ["examples/audios/russian_sample_audio.mp3", "turbo"]
    ]
)
combined_interface = gr.TabbedInterface(
    [txt_interface, image_interface, audio_interface],
    ['Text-to-English', 'Image-to-English', 'Audio-to-English']
)

combined_interface.launch()
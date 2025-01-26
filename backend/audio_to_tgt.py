from openai import OpenAI
import os

whisper_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key = whisper_key)


def src_audio_to_eng_translator(audio_file_input):
    with open(audio_file_input, "rb") as audio_file:
            transcription = client.audio.translations.create(
                model="whisper-1", 
                file=audio_file
            )
    return transcription.text
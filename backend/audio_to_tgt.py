def src_audio_to_eng_translator(audio_file_input):
    transcription = client.audio.translations.create(
    model="whisper-1", 
    file=audio_file_input,
    )
    return transcription.text
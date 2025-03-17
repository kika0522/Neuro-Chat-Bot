from elevenlabs import generate, play, set_api_key, save

API_KEY = ""
TTS_VOICE_ID = "AZnzlk1XvdvUeBnXmlld"
set_api_key(API_KEY)

def tts(text):
    """
    Принимает текстовый файл, возвращает запись в .wav формате
    """
    voice = generate(
    text=text,
    voice=TTS_VOICE_ID,
    model="eleven_multilingual_v2"
    )
    save(voice,'answer.wav')

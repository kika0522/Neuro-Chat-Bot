from elevenlabs import generate, play, set_api_key, save

voice = generate(
  text="Hello! 你好! Hola! नमस्ते! Bonjour! こんにちは! مرحبا! 안녕하세요! Ciao! Cześć! Привіт! வணக்கம்!",
  voice="AZnzlk1XvdvUeBnXmlld",
  model="eleven_multilingual_v2"
)
save(voice,'test.wav')
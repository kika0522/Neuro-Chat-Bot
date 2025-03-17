from TTS.api import TTS

tts=TTS(model_name="tts_models/en/ljspeech/speedy-speech")
tts.tts_to_file(text="Hello world! Hi everyone")
import openai
from elevenlabs import generate, save, set_api_key

API_TTS = "cb9d21635e8b14c097d073eec1eefcf5"
API_KEY = "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"
openai.api_key = API_KEY
set_api_key(API_TTS)

def neuro_request(prompt, max_tokens=256):
    response = openai.Completion.create(
        model='text-davinci-003', 
        max_tokens=256,
        prompt=last_line
        )
    answer = response["choices"][0]["text"]
    return(answer)

def tts(text):
    voice = generate(
    text=text,
    voice="AZnzlk1XvdvUeBnXmlld",
    model="eleven_multilingual_v2"
    )
    save(voice,'answer.wav')

with open('prompt.txt') as f:
    for line in f:
        pass
    last_line = line

    with open('log.txt', "w") as log:

        print(f"PROMPT: {last_line}\n\n")
        answer = neuro_request(prompt=last_line)
        print((f"ANSWER: {answer}"))
        tts(answer)
        log.write(f'USER: {last_line}\nYOU: {answer}')
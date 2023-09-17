import openai
from tts import tts

API_KEY = "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"
openai.api_key = API_KEY

def neuro_request(prompt, max_tokens=256):
    response = openai.Completion.create(
        model='text-davinci-003', 
        max_tokens=256,
        prompt=last_line
        )
    answer = response["choices"][0]["text"]
    return(answer)

with open('prompt.txt') as f:
    for line in f:
        pass
    last_line = line

    with open('log.txt', "w") as log:

        print(f"PROMPT: {last_line}\n\n")
        answer = neuro_request(prompt=last_line)
        answer = str.join(" ", answer.splitlines()) # Убираем переходы на следующую строку.
        print((f"ANSWER: {answer}"))
        tts(answer)
        log.write(f'USER: {last_line}\nYOU:{answer}')
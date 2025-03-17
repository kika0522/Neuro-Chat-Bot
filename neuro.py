import openai
from tts import tts

INPUT_PATH = 'prompt.txt'
API_KEY = "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"
openai.api_key = API_KEY

with open('neuro.txt') as f:
    prompt = f.readline()

with open(INPUT_PATH) as f: #get last line of prompt file
    for line in f:
        pass
    user_input = line
    

def neuro_request(prompt, max_tokens=256):
    response = openai.Completion.create(
        model='text-davinci-003', 
        max_tokens=max_tokens,
        prompt=prompt
        )
    answer = response["choices"][0]["text"]
    return(answer)


with open('log.txt', "a") as log:
    prompt+=user_input
    print(f"PROMPT: {prompt}\n\n")
    answer = neuro_request(prompt=prompt)
    answer = str.join(" ", answer.splitlines()) # Убираем переходы на следующую строку.
    print((f"ANSWER: {answer}"))
    #tts(answer)
    log.write(f'USER: {user_input}\nYOU:{answer}\n\n')
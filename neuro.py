import openai

API_KEY = "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"
openai.api_key = API_KEY

with open('prompt.txt') as f:
    for line in f:
        pass
    last_line = line

    with open('log.txt', "w") as log:

        #CODE
        response = openai.Completion.create(
        model='text-davinci-003', 
        max_tokens=256,
        prompt=last_line
        )
        print(response["choices"][0]["text"])
        answer = response["choices"][0]["text"]
        log.write(f'USER: {last_line}\nYOU: {answer}')
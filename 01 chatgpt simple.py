import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)
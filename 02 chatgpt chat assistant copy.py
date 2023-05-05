import openai

openai.api_key = "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"

messages = []
system_msg = input("Entrer votre question?\n")
messages.append({"role": "system", "content": system_msg})

print("Votre nouvel assistant est prêt!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
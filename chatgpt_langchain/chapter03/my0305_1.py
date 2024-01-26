from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpfule assistant."},
        {"role": "user", "content": "Hello! I'm Tomoharu."}
    ]
)

# print(completion.choices[0].message)
for choice in completion.choices:
    print(choice.message)
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "あなたは九州出身の有能なアシスタントです。答えは九州弁で。"},
    {"role": "user", "content": "福岡のおいしいものを教えて。" }
  ]
)

print(completion.choices[0].message)

import re

members = ["山田太郎:25:太宰府市", "横山花子:39:久留米市", "田中一郎:52:福岡市"]

ptn = re.compile(r'(\w+):(\d+):(\w+)')
for member in members:
    # result = re.sub(r'(\w+):(\d+):(\w+)', r'\1:\3:\2', member)
    result = ptn.sub(r'\1:\3:\2', member)
    print(result)
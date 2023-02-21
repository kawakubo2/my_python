import re

msg = '初めまして。\nよろしくお願いします。'
ptn = re.compile('^.+', re.DOTALL)
results = ptn.findall(msg)
for result in results:
    print(result)
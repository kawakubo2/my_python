import re

s = "私は昨日23:30に寝て、今日6:30に置きました。"

time_pattern = re.compile(r"\d{1,2}:\d{2}")

results = time_pattern.findall(s)
for result in results:
    print(result)
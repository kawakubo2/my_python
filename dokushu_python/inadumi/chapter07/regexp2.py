import re

tel_pattern = '^([0-9]{2,4})-([0-9]{2,4})-([0-9]{4})$'

pattern = re.compile(tel_pattern)

tel = '090-5789-0681'

result = pattern.search(tel)
if result:
    print(result.group(0))
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))

java_pattern = '(Java)[^S]'

pattern = re.compile(java_pattern)

result = pattern.search('私はJavaは好き')

if result:
    print(result.group(0))
    print(result.group(1))

zip_pattern = '〒(\\d{3}-\\d{4})'

pattern = re.compile(zip_pattern)

result = pattern.search('私の会社は〒123-4567です。')

if result:
    print(result.group(1))
    print('start =', result.start(1))
    print('end =', result.end(1))


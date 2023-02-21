import re

ptn = re.compile(r'(?P<name>\w+),(?P<age>\d+),(?P<height>\d+),(?P<department>\w+)')

text = '山田太郎,25,172,開発部'

print(ptn.sub(r'\g<name>,\g<department>,\g<age>,\g<height>', text))

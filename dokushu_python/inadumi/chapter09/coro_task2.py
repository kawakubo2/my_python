import time, os
import requests
import nest_asyncio
nest_asyncio.apply()
import asyncio

async def count_alphabet(file_name):
    def inner(file_name):
        alpabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

        result = {}

        for a in alpabet:
            result[a] = 0

        with open(os.path.dirname(__file__) + '/' + file_name, 'r', encoding='utf_8') as f:
            for line in f:
                line = line.rstrip('\n')
                for c in line:
                    if c in result:
                        result[c] += 1
        return result
    return await loop.run_in_executor(None, inner, file_name)

async def main():
    result = []
    t1 = asyncio.create_task(count_alphabet('a.txt'))
    t2 = asyncio.create_task(count_alphabet('b.txt'))
    t3 = asyncio.create_task(count_alphabet('c.txt'))
    result.append(await t1)
    result.append(await t2)
    result.append(await t3)
    return result

start = time.time()
loop = asyncio.get_event_loop()

result = asyncio.run(main())

end = time.time()
print(result)
print(f'Process Time: {end - start}')
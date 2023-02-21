import asyncio
import time
import nest_asyncio
nest_asyncio.apply()
async def normal_func():
    print('start_normal_func')
    def inner():
        for n in range(100000000):
            if n % 10000000 == 0:
                print(n)
    await loop.run_in_executor(None, inner)
    print('end_normal_func')
async def heavy_process(name, sec):
    print(f'start{name}')
    await asyncio.sleep(sec)
    print(f'end{name}')
    return f'{name}/{sec}'

start = time.time()
loop = asyncio.get_event_loop()
result = loop.run_until_complete(
    asyncio.gather(
        heavy_process('hoge', 2),
        heavy_process('bar', 5),
        normal_func(),
        heavy_process('piyo', 1),
        heavy_process('spam', 3)
    )
)
end = time.time()
print(result)
print(f'Process Time: {end - start}')
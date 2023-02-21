import asyncio
import time
import nest_asyncio
nest_asyncio.apply()
# 疑似的な重い処理
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
        heavy_process('piyo', 1),
        heavy_process('spam', 3)
    )
)
print('main2')
end = time.time()
print(result)
print('main3')
print(f'Process Time: {end - start}')

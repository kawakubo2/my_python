import asyncio
import time
import nest_asyncio
nest_asyncio.apply()
async def heavy_process(name, sec):
    print(f'start{name}')
    await asyncio.sleep(sec)
    print(f'end{name}')
    return f'{name}/{sec}'

async def main():
    t1 = asyncio.create_task(heavy_process('hoge', 2))
    t2 = asyncio.create_task(heavy_process('bar', 5))
    t3 = asyncio.create_task(heavy_process('piyo', 1))

    print(await t1)
    print(await t2)
    print(await t3)

start = time.time()
loop = asyncio.get_event_loop()

asyncio.run(main())

end = time.time()
print(f'Process Time: {end - start}')
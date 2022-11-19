import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
	task1 = asyncio.create_task(say_after(1,'Hello'))
	task2 = asyncio.create_task(say_after(2,'world'))
	print('Started at %s' %time.strftime('%X'))
	await task1
	await task2
	print('Finished at %s' %time.strftime('%X'))

asyncio.run(main())
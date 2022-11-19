import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
	print('Started at %s' %time.strftime('%X'))
	await say_after(1,'Hello')
	await say_after(2,'world')
	print('Finished at %s' %time.strftime('%X'))

asyncio.run(main())
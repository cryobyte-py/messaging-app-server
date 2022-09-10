import aiohttp
import asyncio

async def connect():
    async with aiohttp.ClientSession() as session:
        async with session.post("http://192.168.1.109:8080/test", json = {"payload":1234}) as resp:
            print(resp)

asyncio.run(connect())
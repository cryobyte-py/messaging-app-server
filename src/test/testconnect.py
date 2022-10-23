import aiohttp
import asyncio

async def slash():
    resp = await session.get("http://127.0.0.1:8080/")
    return resp

async def testcon():
    resp = await session.post("http://127.0.0.1:8080/test/")
    return resp

session = aiohttp.ClientSession()

while True:
    i = input("\n 0- / 1- TEST 2- LOGIN 3- REGISTER\n \n")

    if i == 0:
        print(slash().text)

    if i == 1:
        print(testcon().text)
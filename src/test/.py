import sys
from aiohttp import web
import asyncio
import json
import sqlite3
sys.path.append("C://Users//lenovo//Desktop//messaging-app-server//appserver//src")
from servclass import MessagingServer
database = 0
settings = {}
MyServer = MessagingServer(settings=settings, database=database)
routes = web.RouteTableDef()

routes.post("/register/")
async def register(response):
    args = response.json()
    

@routes.post("/login/")
async def login(response):
    args = response.json()

@routes.post("/test")
async def test(request):
    args = await request.json()
    print(args)
    return web.Response(status=200)

@routes.get("/")
async def testget(request):
    await print(request)
    await web.Response(status=200, text="Hello")

app = web.Application()
app.add_routes(routes)
web.run_app(app)
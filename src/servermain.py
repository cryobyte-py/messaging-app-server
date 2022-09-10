from aiohttp import web
import asyncio
import json
import sqlite3

conn = sqlite3.connect("assets/database.db")
cur = conn.cursor()
routes = web.RouteTableDef()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata ( 
INTEGER PRIMARYKEY AUTOINCREMENT userid NOT NULL AUTO_INCREMENT,
username varchar(32) NOT NULL, 
PASSWORD password NOT NULL, 
EMAIL email NOT NULL
)""")

loginTemp = {
    "EMAIL" : "",
    "PASSWORD" : ""
}
msgTemp  = {
    "USERID" : "",
    "CONTEXT" : ""
}

@routes.post("/register/")
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
    await web.Response(status=200)

app = web.Application()
app.add_routes(routes)
web.run_app(app)
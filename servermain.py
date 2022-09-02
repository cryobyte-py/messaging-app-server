from aiohttp import web
import asyncio
import json
import sqlite3

#conn = sqlite3.connect("assets/database.db")
#cur = conn.cursor()
routes = web.RouteTableDef()

#cur.execute("""CREATE TABLE IF NOT EXISTS userdata ( PRIMARYKEY userid, string username, PASSWORD password)""")

loginTemp = {
    "USERNAME" : "",
    "PASSWORD" : ""
}
msgTemp  = {
    "USERID" : "",
    "CONTEXT" : ""
}

@routes.post("/register/")
async def register():
    pass
@routes.post("/login/")
async def login():
    pass
@routes.post("/test")
async def test(request):
    args = await request.json()
    print(args)
    return web.Response(text="OK")
@routes.get("/")
async def testget(request):
    return web.Response(text="balls")

app = web.Application()
app.add_routes(routes)
web.run_app(app)
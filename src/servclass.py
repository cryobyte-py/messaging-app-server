from aiohttp import web
import asyncio
import json
import sqlite3
import os

class MessagingServer():
    version = "0.0.1"
    def __init__(self, settings, database) -> None:
        try: 
            self.settings = settings
            self.database = database
        except Exception as e:
            print(f"An error has occured: {e}")
            os.sys("pause")
        finally: print(f"Initialized server. Version: {MessagingServer.version}")
    
    def register(args):
        print(args)
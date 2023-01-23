from aiohttp import web
import asyncio
import sqlite3
import json
import os
from pathlib import Path
from dotenv import load_dotenv
from cryptography.fernet import Fernet

class MessagingApp():

    class MAExceptions():
        class InvalidCredentials(Exception):
            pass
        class RegistryError(Exception):
            pass
    class Database():

        databasestart = f"""
CREATE TABLE IF NOT EXISTS USERS (
    USERID INTEGER PRIMARYKEY AUTO_INCREMENT,
    USERNAME STRING NOT NULL,
    PASSWORD STRING NOT NULL,
    EMAIL STRING NOT NULL
)
""" 
        def __init__(self, db):
            self.db = Path(db)
            self.conn = sqlite3.connect(self.db)
            self.cur = self.conn.cursor()
            self.cur.execute(self.databasestart)

        def insertIntoDatabase(self, action, args: list):
            if action == "register":
                self.cur.execute(f"INSERT INTO USERS (USERNAME, PASSWORD, EMAIL) VALUES ('{args[0]}', {str(args[1]).strip('b')}, '{args[2]}')")
                self.conn.commit()

        def retrieveFromDatabase(self, args: dict):
            self.cur.execute(f"SELECT * FROM USERS WHERE {args['column']} = '{args['data']}'")
            return self.cur.fetchall()

    def __init__(self, settings) -> None:
        # Settings
        self.settings = Path(settings)
        with open(self.settings,"rt") as f:
            self.settings = json.load(f)
        self.db = MessagingApp.Database(db=self.settings["config"]["databasePath"])
        # Encryption system
        self.env = Path(self.settings["config"]["envPath"])
        load_dotenv(dotenv_path= self.env)
        self.fernet = Fernet(os.getenv("ENCRYPTION_KEY"))
       

    def userRegister(self, args: dict):
        """Takes the dictionary converted from the JSON file from the client's POST request and sends it into the database for registry."""
        try:
            username = args["USERNAME"]
            password = args["PASSWORD"]
            email = args["EMAIL"]
        except:
            raise ValueError("Invalid arguments!")

        # Encrypt password using ENCRYPTION_KEY
        pwd_enc = self.fernet.encrypt(password.encode())

        # validate email
        x = email.split("@")
        if len(x) != 2:
            if str(email).find(".co") or str(email).find(".org") or str(email).find(".edu") or str(email).find(".net") == None:
                raise self.MAExceptions.RegistryError("Invalid email!")
        arguments =  [username,pwd_enc,email]
        self.db.retrieveFromDatabase(args={'column' : 'USERNAME', 'data' : username}) and self.db.retrieveFromDatabase(args={'column' : 'EMAIL', 'data' : email}) == None
        if self.db.cur.fetchall is None:
            self.db.insertIntoDatabase(action="register", args=arguments)
        else:
            raise self.MAExceptions.RegistryError("User already exists!")
    def userLogin(self, args: dict):
        pass

    async def initApp(self):
        pass
from MessagingApp import MessagingApp
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path("appserver//assets//.env"))
key = os.getenv("ENCRYPTION_KEY")
enc = Fernet(key)

myApp = MessagingApp(settings="appserver//assets//settings.json")
payload = {
    "USERNAME" : "JohnDoe123",
    "PASSWORD" : "pAsSwOrD987_",
    "EMAIL" : "johndoe123@example.com"
}
try: myApp.userRegister(args=payload)
except MessagingApp.MAExceptions.RegistryError as e:
    print(f"Could not complete registration: {e}")

args = {
    'column' : 'USERNAME',
    'data' : 'JohnDoe123'
}
data = myApp.Database.retrieveFromDatabase(args=args, self = myApp.db)[0]

username = data[1]
password = enc.decrypt(data[2]).decode()
email = data[3]

print(f"""
USERNAME : {username}
PASSWORD : {password}
EMAIL    : {email}
""")

import json
import os
#read json file
try:
    if os.path.exists("accounts.json"):
        with open("accounts.json", "r") as f:
            account = json.load(f)
    else:
        raise FileNotFoundError("accounts.json not found.")
except (json.JSONDecodeError, FileNotFoundError) as e:
    print(f"Error loading accounts: {e}")
    account = {}
def login():
    while True:
        user = input("username: ")
        password = input("password: ")
        if user in account and account[user]["password"]==password:
            print("Log in successfully")
            return user, account
        else:
            print("Try again")
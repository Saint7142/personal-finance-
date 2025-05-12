import json
import os
#read data from json
if os.path.exists("accounts.json"):
    with open("accounts.json", "r") as f:
        account = json.load(f)
else:
    account = {
    "user1": {"password":"1234", "balance":0}
    }
#Log in
while True:
    user = input("username: ")
    password = input("password:")
    if user in account and account[user]["password"]==password:
        print("Log in successfully")
        break
    else:
        print("Try again")
#input&output
while True:
    method = (input("Add income(Press 1), Add expense(Press 2), End service(Press 3 ): "))
    match method:
        case "1":                
            income = int(input("Add income: "))
            account[user]["balance"]+=income
            print(f"Total money: {account[user]['balance']:,}")
        case "2":
            expense = int(input("Money withdraw: "))
            if account[user]["balance"]>=expense:
                account[user]["balance"]-=expense
                print(f"Total money: {account[user]['balance']:,}")
            else:
                print("Not enough balance")
        case "3":
            print("End of service")
            break
        case _:
             print("Try again")
#save data
with open("accounts.json", "w") as f:
    json.dump(account, f, indent=4)
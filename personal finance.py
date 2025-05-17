#other module imported
import log_in
import method
import json
#Log in
user, account = log_in.login()
print("---STATUS---")
print(f"Name: {user}")
print(f"balance: {account[user]['balance']}")

#input&output
while True:
    selection = (input("Add income(Press 1), Add expense(Press 2), End service(Press 3 ): "))
    match selection:
        case "1":                
            method.addmoney(account, user)
        case "2":
            method.withdraw(account, user)
        case "3":
            print("End of service")
            break
        case _:
             print("Try again")
#save data
with open("accounts.json", "w") as f:
    json.dump(account, f, indent=4)

#calculate method
def addmoney(account, user):
    income = int(input("Income: "))
    account[user]["balance"]+=income
    print(f"Total money: {account[user]['balance']:,}")
def withdraw(account, user):
    expense = int(input("Money withdraw: "))
    if account[user]["balance"]>=expense:
        account[user]["balance"]-=expense
        print(f"Total money: {account[user]['balance']:,}")
    else:
        print("Not enough balance")
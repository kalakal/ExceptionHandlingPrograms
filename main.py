class BalanceException(Exception):
    pass


def checkbalance():
    money = 10000
    withdraw = int(input("Enter The Amount"))
    try:
        balance = money - withdraw
        if(balance<=2000):
            raise BalanceException("insufficient balance")
        print(balance)
    except BalanceException as be:
        print(be)


checkbalance()

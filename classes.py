class User:
    def __init__(self) -> None:
        pass



class Bank:
    def __init__(self, money_balance) -> None:
        self.money_balance = money_balance


    #withraw function change name ng attributes kapag mali
    def withdraw(self, user, amount):
        user.user_money += amount
        self.money_balance -= amount

    #deposit to
    def deposite(self, user, amount):
        user.user_money -= amount
        self.money_balance += amount




class User:
    def __init__(self, first_name, middle_name, last_name, password, user_money:int):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__password = password
        self.__user_money = user_money

    def full_name(self):
        return f'{self.__first_name} {self.__middle_name} {self.__last_name}'
    
    def get_password(self):
        return f'{self.__password}'
    
    def get_user_money(self):
        return f'{self.__user_money}'


class Bank:
    def __init__(self, money_balance) -> None:
        self.money_balance = money_balance

    #withraw function change name ng attributes kapag mali
    """
    def withdraw(self, user, amount):
        user.get_user_money() += amount
        self.money_balance -= amount

    #deposit to
    def deposite(self, user, amount):
        user.get_user_money() -= amount
        self.money_balance += amount"""

b1 = Bank(money_balance=100)
u1 = User(first_name='Juan', middle_name= 'J.', last_name='Tamad', password= 123, 50)

print(u1.get_user_money())

#withdraw kuha or plus
#deposit minus or bawas
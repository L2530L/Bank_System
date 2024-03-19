class User:
    def __init__(self, first_name, middle_name, last_name, password, user_money:int):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__password = password
        self.__user_money = user_money

       
    @property    
    def full_name(self):
        return f'{self.__first_name} {self.__middle_name} {self.__last_name}'

    @property
    def get_password(self):
        return f'{self.__password}'
    
    @property
    def money(self):
        return int(self.__user_money)
    
    @money.setter
    def money(self, user_money):
        (self.__user_money) = user_money
    


class Bank:
    def __init__(self, money_balance) -> None:
        self.money_balance = money_balance

    #withraw function change name ng attributes kapag mali
    
    
    def withdraw(self, user, amount):
        user.money += int(amount)
        self.money_balance -= amount

    #deposit to
    def deposit(self, user, amount):
        user.money -= int(amount)
        self.money_balance += amount

b1 = Bank(money_balance=100)
u1 = User(first_name='Juan', middle_name= 'J.', last_name='Tamad', password= 123, user_money=100)



b1.withdraw(u1, 100)
print(f"user: {u1.money}")
print (f"bank: {b1.money_balance}")

#withdraw kuha or plus
#deposit minus or bawas
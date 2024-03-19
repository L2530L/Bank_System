from classes import User, Bank

b1 = Bank(money_balance=100)
u1 = User(first_name='Juan', middle_name= 'J.', last_name='Tamad', password= 123, user_money=100)

b1.withdraw(u1, 100)
print(f"user: {u1.money}")
print (f"bank: {b1.money_balance}")

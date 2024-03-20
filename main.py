from classes import User, Bank


u1 = User(first_name='Juan', middle_name= 'J.', last_name='Tamad', password= 123, user_money=2000)
u2 = User(first_name='TAE', middle_name= 'D.', last_name='Tiong', password= 555, user_money=1500)
b1 = Bank(money_balance=2000)
b2 = Bank(money_balance=50)
while True:
    

    
    b1.withdraw(u1, 100)

    
    b2.deposit(u2, 150)

    print(u1.full_name)
    print(f"user: {u1.money}")
    print (f"bank: {b1.money_balance}\n")

    print(u2.full_name)
    print(f"user: {u2.money}")
    print (f"bank: {b2.money_balance}\n")

    exit = input("enter EXIT\n")
    if exit == "exit":
        break 
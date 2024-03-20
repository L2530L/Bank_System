from classes import User, Bank, Account



bank = Bank()

while True:
    #This is the first interface
    choice = input("""
What do you want to do?
1.) Create Account
2.) Login
3.) Exit
""")
    
    if choice == '1':
        bank.create_account()
    elif choice == '2':
        account_number = int(input("Enter account number: "))
        pin = int(input("Password: "))


        login = bank.login(account_number, pin, bank)
        if login:
            while True:
                acc = bank.accounts[bank.find_account(account_number)]
                choice = acc.account_interface()
                if choice == '1':     
                    balance = bank.get_account(account_number)
                    amount = int(input("Amount: "))
                    acc.deposit(amount)
                    print(f"Your balance is now {acc.balance}")

                elif choice == '2':     
                    balance = bank.get_account(account_number)
                    amount = int(input("Amount: "))
                    acc.withdraw(amount)
                    print(f"Your balance is now {acc.balance}")

                elif choice == '3':
                    print(f"Your balance is now {acc.balance}")

                elif choice == '4':
                    break


                

    elif choice == '3':
        break

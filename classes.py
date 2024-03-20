class User:
    def __init__(self, first_name:str, middle_name:str, last_name:str,user_money:int, password):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__password = password
        self.__user_money = user_money


    @property
    def first_name(self):
        return f"{self.__first_name}"
    
    @property
    def middle_name(self):
        return f"{self.__middle_name}"
    
    @property
    def last_name(self):
        return f"{self.__last_name}"
    
    @property    
    def full_name(self):
        return f'{self.__first_name} {self.__middle_name} {self.__last_name}'
    

    @full_name.setter
    def full_name(self, name):
        last, first, middle = name.split(" ")
        self.__last_name = last
        self.__first_name = first
        self.__middle_name = middle       

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
    def __init__(self) -> None:
        self.accounts = []     #List account

    #used for finding account index using account number:: checker=account nummber used to find
    def find_account(self, checker):
        counter = 0
        for account in self.accounts:
            if account.account_number == checker:
                return counter
                break
            else:
                counter += 1
            

    def create_account(self):
        full_name = input("What is your full name (Last name, First name, Middle): ")
        pin = int(input("What is the pin number: "))

        #Generate different account number
        account_num = len(self.accounts) + 1 * 3

        self.accounts.append(Account(full_name, 0, account_num, pin ))
        print("Created!")
        print(f"Your account number is {account_num}")


    #Check if the login is correct or no :: acount_number for finding account || pin to check password 
    #account= the list of accounts
    def login(self,account_number, pin ,account):
        index = self.find_account(account_number)
       
        if self.check_account(account_number) and self.check_password(account.accounts[index], pin):
            print("Success")
            return True
        else:
            print("Somethin wrong")
            return False

    
    def check_password(self,account, password):
        if password == account.password:
            return True
        else:
            return False
    

    def check_account(self, account_number):
        finder = 0
        for account in self.accounts:
            if account.account_number == account_number:
                finder += 1
                if finder == 1:
                    return True
                else:
                    print("No account with that number")
                    return False
            

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account.balance
            else:
                print("No account with that number")
                return False
        


class Account():
    def __init__(self, user, balance:float, account_number, password:int) -> None:
        self.user = user
        self.balance = balance
        self.account_number = account_number
        self.password = password

    def account_interface(self):
        choice = input("""
What to do?
1.) deposit
2.) Withdraw
3.) Check balance
4.) Exit
                           """)
        return choice
            

    def withdraw(self, amount):
        self.balance -= amount

    #deposit to
    def deposit(self, amount):
        self.balance += amount



    

#withdraw kuha or plus
#deposit minus or bawas

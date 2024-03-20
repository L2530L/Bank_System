class User:
    def __init__(self, first_name:str, middle_name:str, last_name:str, password, user_money:int):
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
    
    #set the full name and spliting the fullname to 
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


    def create_account(self):
        self.full_name = input("What is your name (Lastname Firstname Middlename): ")
        #pass
        
      
        

class Bank:
    def __init__(self, money_balance:int) -> None:
        self.money_balance = money_balance

    #withraw function change name ng attributes kapag mali
    
    
    def withdraw(self, user, amount):
        user.money += int(amount)
        self.money_balance -= amount

    #deposit to
    def deposit(self, user, amount):
        user.money -= int(amount)
        self.money_balance += amount



#withdraw kuha or plus
#deposit minus or bawas
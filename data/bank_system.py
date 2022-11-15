from random import randint

class Bank:
    name = 'The wealthy bank'
    users = []

    def user_update(self, user):
        self.users.append(user)

    def check_auth(self, name, account_number):
        for i in range(len(self.users)):
            if name in self.users[i].account.values() and account_number in self.users[i].account.values():
                print()
                print('authorization Successfully')
                return self.users[i]

class user:
    account = {}

    def __init__(self, name, deposit):
        self.account['account_number'] = randint(10000, 99999)
        self.account['name'] = name
        self.account['holding'] = deposit

    def withdraw(self, amount):
        if self.account['holding'] >= amount:
            self.account['holding'] -= amount
            print()
            print("the sum of {} has bee withdrawn form your account balance". format(amount))
            self.balance()
        else:
            print()
            print("Not enough money")
            self.balance()
    
    def balance(self):
        print()
        print("your current balance is {} ".format(self.account['holding']))

    def deposit(self, amount):
        self.account['holding'] += amount
        print()
        print("the sum of {} has been add to your account".format(amount))
        self.balance()

bank = Bank()
print()
print('welcome to {} !'.format(bank.name))
print()
runing = True

while runing :
    print()
    print("""
    Choose yor optioin 
    1. Open new account
    2. Open Your Existing accoont
    3. Exit

    """)

    choice = int(input("1, 2, 3 "))

    if choice == 1:
        print('Create an accoun, please fill in the informaion ')
        print()
        user  = user(input('Name: '), int(input('First deposit amount:')))
        bank.user_update(user)
        print()
        print('Account created, you account number is ', user.account['account_number'])
    elif choice == 2:
        print()
        print("Access to your account please identify yourselfe")
        print()
        name = input('Name: ')
        account_number = int(input('Account number: '))
        current_user = bank.check_auth(name, account_number)
        if current_user:
            print()
            print('Welcome {}'.format(current_user.account['name']))
            acc_open = True
            while acc_open:
                print()
                print(
                    """Choose the option
                    1.Withdraw
                    2.Deposit
                    3.Check Balance
                    4. Exit

                    """ )
                acc_choice = int(input('1, 2, 3, 4 '))
                if acc_choice == 1:
                    print()
                    current_user.withdraw(int(input('Withdraw amount: ')))
                elif acc_choice == 2:
                    print()
                    current_user.deposit(int(input('Deposit amount: ')))
                elif acc_choice == 3:
                    current_user.balance()
                elif acc_choice == 4:
                    print()
                    print('Thank you ')
                    current_user = ''
                    acc_open = False
            else:
                print("authentication fail")    
                print('account not found')
                continue
    elif choice == 3:
        print()
        print('See you have a nice day')
        runing = False
        

#https://github.com/bizarrenebula/Simple-Banking-System/blob/master/main.py


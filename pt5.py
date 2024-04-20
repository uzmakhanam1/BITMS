#calling functions in dictionary

#witiout parameter
'''def uzma():
    return "this is my bank balance"
#initialize dictionary
#checck for function name as key
test_dict={"fname":uzma,"age":50,"address":"salem"}
#printing original dictionary
print("the original dictionary is:"+str(test_dict))
#calling function using brackets
res=test_dict['fname']()
#printing result
print("the required call result :"+str(res))#based on return type our res data type is given ie str'''




#with parametr (here as we are not storing function call value  in variable ie like (res) we dont need to use return value .direct use print
'''def uzma(a,b):
    print("my result bank balance=",a+b)
#initialize dictionary
#checck for function name as key
test_dict={"fname":uzma,"age":50,"address":"salem"}
#printing original dictionary
print("the original dictionary is:"+str(test_dict))
#calling function using brackets
test_dict['fname'](10,20)'''



#banking program

'''def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds!")
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

def deposit(account, amount):
    account['balance'] += amount
    account['transactions'].append(f"Deposit: ${amount}")
    print(f"Deposit successful. Remaining balance: ${account['balance']}")

def get_balance(account):
    return account['balance']

def get_transaction_history(account):
    return account['transactions']

# Create an account dictionary
account = {
    'balance': 1000,
    'transactions': []
}

# Dictionary to map user choices to functions
choices = {
    '1': deposit,
    '2': withdraw,
    '3': get_balance,
    '4': get_transaction_history
}

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '5':
        print("Exiting program.")
        break

    if choice in choices:
        if choice == '1' or choice == '2':
            amount = float(input("Enter amount: "))
            choices[choice](account, amount)#passing parameters if choice 1 or 2
        else:
            print(choices[choice](account))# if choice is 3 or 4 then pass the account as paramter
    else:
        print("Invalid choice. Please try again.")'''
        
        

# with some credientials for single user

'''email = "sadiuzma"
pwd = "1234"

uemail = input("Enter the email: ")
upwd = input("Enter the password: ")

if email != uemail or pwd != upwd:
    print("Invalid email or password")
else:
    def withdraw(account, amount):
        if amount > account['balance']:
            print("Insufficient funds!")
        else:
            account['balance'] -= amount
            account['transactions'].append(f"Withdrawal: ${amount}")
            print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

    def deposit(account, amount):
        account['balance'] += amount
        account['transactions'].append(f"Deposit: ${amount}")
        print(f"Deposit successful. Remaining balance: ${account['balance']}")

    def get_balance(account):
        return account['balance']

    def get_transaction_history(account):
        return account['transactions']

    # Create an account dictionary
    account = {
        'balance': 1000,
        'transactions': []
    }

    # Dictionary to map user choices to functions
    choices = {
        '1': deposit,
        '2': withdraw,
        '3': get_balance,
        '4': get_transaction_history
    }

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '5':
            print("Exiting program.")
            break

        if choice in choices:
            if choice == '1' or choice == '2':
                amount = float(input("Enter amount: "))
                choices[choice](account, amount)  # passing parameters if choice 1 or 2
            else:
                print(choices[choice](account))  # if choice is 3 or 4 then pass the account as parameter
        else:
            print("Invalid choice. Please try again.")'''


#for multiple users

'''def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds!")
    elif  account['count']>=3:
        print("transcation limit exceeded")
        
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        account['count']+=1
        print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

def deposit(account, amount):
    account['balance'] += amount
    account['transactions'].append(f"Deposit: ${amount}")
    print(f"Deposit successful. Remaining balance: ${account['balance']}")

def get_balance(account):
    return account['balance']

def get_transaction_history(account):
    return account['transactions']

# Create an account dictionary
account = {
    'balance': 1000,
    'transactions': [],
    'count':0
}

# Dictionary to map user choices to functions
choices = {
    '1': deposit,
    '2': withdraw,
    '3': get_balance,
    '4': get_transaction_history
}
details = {
    'user': ['siri','sanjana','uzma'],
    'pass' : ['1','2','3']
}
username = input("enter the username")
passwd = input("enter the password")
if username in details['user'] and passwd and details['pass']:
    print("successful")
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '5':
            print("Exiting program.")
            exit()

        if choice in choices:
            if choice == '1' or choice == '2':
                amount = float(input("Enter amount: "))
                choices[choice](account, amount)
            else:
                print(choices[choice](account))
        else:
            print("Invalid choice. Please try again.")
else:
    print("invalid")
    exit()
'''


#ATM
'''            
atm = {'balance': 10000, 'transaction': [], 'n': 1}

def withdraw(atm):
    if atm['n']<=2:
        amount = float(input("Enter amount to be withdrawn:"))
        if amount <= atm['balance']:
            atm['n'] += 1
            atm['balance']-= amount
            print(f"Available balance: {atm['balance']}")
            atm['transaction'].append(f"Withdrawn: ${amount}")
        else:
            print("Insufficient funds")
    else:
        print("Transaction limit exceeded")

def balance(atm):
    return atm['balance']
choices = {'1': withdraw, '2': balance}
def acess():
    while True:
        print("1. Withdraw")
        print("2. Balance")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '3':
            print("Exited successfully")
            break
        elif choice == '1':
            choices[choice](atm)
        elif choice == '2':
            print("Current balance:", choices[choice](atm))
        else:
            print("Invalid choice")

details={'email':{}}
email={"abcd":"1234","pqrs":"5678","xyz":"9087"}
user_email=input("enter email")
user_password=input("enter password")
if(user_email in email and email[user_email]==user_password):
    print("login succesfull")
    acess()
else:
    print("invalid credentials")'''



#banking using classes with compile time inputs(WE CAN EVEN CHANGE THE NAME OF SHELL)

'''class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.transactions = []

    def withdraw(shetty, amount):
        if amount > shetty.balance:
            print("Insufficient funds!")
        else:
            shetty.balance -= amount
            shetty.transactions.append(f"Withdrawal: ${amount}")
            print(f"Withdrawal successful. Remaining balance: ${shetty.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount}")
        print(f"Deposit successful. Remaining balance: ${self.balance}")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

# Example usage:
account = BankAccount(1000)
print("Balance:", account.get_balance())
account.deposit(500)
account.withdraw(200)
account.withdraw(1000)
print("Balance:", account.get_balance())
print("Transaction History:", account.get_transaction_history())'''



#with runtime time inputs
class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.transactions = []

    def withdraw(shetty, amount):
        if amount > shetty.balance:
            print("Insufficient funds!")
        else:
            shetty.balance -= amount
            shetty.transactions.append(f"Withdrawal: ${amount}")
            print(f"Withdrawal successful. Remaining balance: ${shetty.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount}")
        print(f"Deposit successful. Remaining balance: ${self.balance}")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions


# Example usage:
account = BankAccount(1000)
print("Balance:", account.get_balance())
n=int(input("enter the deposite"))
account.deposit(n)
n=int(input("enter the withdrawal amount"))
account.withdraw(n)
n=int(input("enter the withdrawal amount"))
account.withdraw(n)
print("Balance:", account.get_balance())
print("Transaction History:", account.get_transaction_history())





#f=k+[(13*m-1)/5]+D+[D/4]+[C/4]-2*C(zellers formula)



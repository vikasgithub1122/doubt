class Bank:
    bank_name='SBI'
    min_balance=500
    
    def __init__(self, accountNumber, name, balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance
        
    def deposit (self, amount):
        self.balance +=amount
        print(f'deposit successfully')
        
    def details(self):
        print(f"""account{self.accountnumber}")
        name{self.name}
        balance{self.balance}""")
        
    def withdrawl(self, amount):
        self.balance -=amount
        print(f'Withdraw successfully')
        
        # if self.balance<Bank.min_balance:
        #     print("Please deposit amount with in a month, balance is very low")
        # elif amount>self.balance:
        #     print("your balance is", self.balance)
        # elif amount<self.balance:
        #     self.balance -=amount
    
b=Bank(1001, 'virat', 6500)
print("W: Withdrawl")
print("D: deposit")
print("A:Details")
print("q:Exit")

while True:
    key=input("Enter a Key :")
    if key=="W":
        amount=float(input("Enter a amount"))
        b.withdrawl(amount)
    elif key=="D":
        amount=float(input("Enter a amount:"))
        b.deposit(amount)
    elif key=="A":
        b.details()
    elif key=='q':
        break
    
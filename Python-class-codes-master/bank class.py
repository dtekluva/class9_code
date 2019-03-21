num_accs=[0]
class Banking():
    balance=0.0
    num_accs[0]+=1
    def __init__(self,username,phone,email):
        self.username=username
        self.phone=phone
        self.email=email
        self.account=""
        

    def createAcc(self,num_accs):
        accountnumber=1000000000
        self.account=accountnumber+num_accs[0]
        num_accs[0]+=1

    def checkBalance(self,accn):
        return self.balance
    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if self.balance<amount:
            print("Insufficient funds")

        else:
            self.balance-=amount
            print("You have withdrawn ",amount," and your balance is",self.balance,)
            return self.balance
            
cust_obj=Banking("frank ","08031346306","qwerty@yahoo.com")
cust_obj2=Banking("James ","08031346306","qwerty@yahoo.com")
cust_obj3=Banking("Affiong ","08031346306","qwerty@yahoo.com")
account_no=cust_obj.createAcc(num_accs)
print(cust_obj.username,"   :  ",cust_obj.checkBalance(account_no)," Acct no :   ",cust_obj.account, )
cust_obj.withdraw(25000)

cust_obj.deposit(500000)
cust_obj.withdraw(1000)


account_no=cust_obj2.createAcc(num_accs)
print(cust_obj2.username,"   :  ",cust_obj2.checkBalance(account_no)," Acct no :   ",cust_obj2.account, )
cust_obj2.withdraw(5000)
cust_obj2.deposit(200000)
cust_obj2.withdraw(1000)

account_no=cust_obj3.createAcc(num_accs)
print(cust_obj3.username,"   :  ",cust_obj3.checkBalance(account_no)," Acct no :   ",cust_obj3.account, )
cust_obj3.withdraw(5000)
cust_obj3.deposit(700000)
cust_obj3.withdraw(102300)

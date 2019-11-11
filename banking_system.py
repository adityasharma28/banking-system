import pickle
import os
class Banking:
    def __init__(self):
        self.Check()
        self.Name=input("Enter Name:")
        while True:
            print("Enter Type of Account:\n S for Saving and C for Current")
            self.Type=input()
            if self.Type=='S' or self.Type=='C':
                break
            print("Enter Valid Accout Type:")
        while True:
            print('''Enter Amount\n 1.For Saving Account Minimum Balance 5000\n
                  2.For Current Account Minimum Balance 10000''')
            self.Amount=int(input())
            if self.Type=='S' and self.Amount>=5000 or self.Type=='C' and self.Amount>=10000:
                break
        self.Write()
    def Check(self):
        try:
            file=open('Record.bin','rb')
            while True:
                s=pickle.load(file)
        except FileNotFoundError:
            self.AccNo=12345
        except EOFError:
            self.AccNo=s.AccNo+1
            file.close()
    def Write(self):
        try:
            file=open("Record.bin",'ab')
            pickle.dump(self,file)
        except FileNotFoundError:
            print("File Not Found")
        else:
            file.close()
    @staticmethod
    def Display():
        print('----------------------------------------------------------------------')
        print('{:>10}{:>20}{:>10}{:>15}'.format('AccNo','Name','Type','Amount'))
        print('----------------------------------------------------------------------')
        try:
            file=open("Record.bin",'rb')
            while True:
                s=pickle.load(file)
                print('{:>10}{:>20}{:>10}{:>15}'.format(s.AccNo,s.Name,s.Type,s.Amount))
        except FileNotFoundError:
            print("File Not Found")
        except EOFError:
            file.close()
    @staticmethod
    def Deposit(acc):
        try:
            file1=open("Record.bin",'rb')
            file2=open('Temp.bin','wb')
            while True:
                s=pickle.load(file1)
                if s.AccNo==acc:
                    am=int(input("Enter Amount:"))
                    s.Amount=s.Amount+am
                pickle.dump(s,file2)
        except FileNotFoundError:
            print("File Not Found")
        except EOFError:
            file1.close()
            file2.close()

        os.remove('Record.bin')
        os.rename('Temp.bin','Record.bin')
    @staticmethod
    def Withdrawl(acc):
        try:
            file1=open("Record.bin",'rb')
            file2=open('Temp.bin','wb')
            while True:
                s=pickle.load(file1)
                if s.AccNo==acc:
                    while True:
                        am=int(input("Enter Amount:"))
                        if s.Type=='S' and s.Amount-am>=5000 or s.Type=='C' and s.Amount-am>=10000:
                            s.Amount=s.Amount-am
                            break
                        else:
                            print("Insufficent Fund in Account")
                pickle.dump(s,file2)
        except FileNotFoundError:
            print("File Not Found")
        except EOFError:
            file1.close()
            file2.close()
        os.remove('Record.bin')
        os.rename('Temp.bin','Record.bin')

    @staticmethod
    def Update(acc):
        try:
            file1=open("Record.bin",'rb')
            file2=open('Temp.bin','wb')
            f=0
            while True:
                s=pickle.load(file1)
                if s.AccNo==acc:
                    f=1
                    print(s.AccNo,s.Name,s.Type,s.Amount,sep='\t')
                    s.Name=input("Enter new name:")
                pickle.dump(s,file2)
                    
        except FileNotFoundError:
            print("File Not Found")
        except EOFError:
            file1.close()
            file2.close()
        os.remove('Record.bin')
        os.rename('Temp.bin','Record.bin')       

while True:
    n=int(input('''Enter Your Choice:\n1.Create\n2.Display all Account
3.Deposit\n4.Withdrawl\n5.Update\n6.Exit\n'''))
    if n==1:
        b=Banking()
    elif n==2:
        Banking.Display()
    elif n==3:
        acc=int(input("Enter Account Number:"))
        Banking.Deposit(acc)
    elif n==4:
        acc=int(input("Enter Account Number:"))
        Banking.Withdrawl(acc)
    elif n==5:
        acc=int(input("Enter account number:"))
        Banking.Update(acc)
    else:
        break

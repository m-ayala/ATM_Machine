import sys

class Bank():

    def __init__(self, name, card_number, pin, checking_balance, savings_balance):
        self.name = name
        self.number = card_number
        self.PIN = pin
        self.acc = ""
        self.blocked = False
        self.checking = checking_balance
        self.savings = savings_balance

    def deposit(self, amt):
        if self.acc == "savings":
            self.savings = self.savings + int(amt)
        else:
            self.checking = self.checking + int(amt)

    def withdraw(self, amt):
        if self.acc == "savings":
            if self.savings >= int(amt):
                self.savings = self.savings - int(amt)
                print self.savings
            else:
                print("Overdrawn, request not processed")
        else:
            if self.checking >= int(amt):
                self.checking = self.checking - int(amt)
                print self.checking
            else:
                print("Overdrawn, request not processed")

class Machine():

    def __init__(self, user, cash):
        self.user = user
        self.cash_tray = cash

    def card(self, name, number):
        for i in range(len(obj)):
            if obj[i].name == name and obj[i].number == number:
                if obj[i].blocked:
                    return "Blocked"
                self.user = i
                print "Found card"
                print "Directing to accounts"
                return True
                break
        if self.user == None:
            print("Card Not Found")
            return False

    def check_pin(self, pin):
        if pin != obj[self.user].PIN:
            return "denied"
        else:
            return "given"

    def set_acc(self, acc):
        if acc == "S":
            obj[self.user].acc = "savings"
        elif acc == "C":
            obj[self.user].acc = "checking"
        else:
            print "Unidentified account"

    def display(self):
        if obj[self.user].acc == "savings":
            print ("Savings account balance is: " + str(obj[self.user].savings))
        else:
            print ("checking account balance is: " + str(obj[self.user].checking))

    def withdraw(self, amt):
        if int(amt)>=self.cash_tray:
            print "No cash in ATM!"
        else:
            obj[self.user].withdraw(amt)
            self.cash_tray = self.cash_tray - int(amt)

    def deposit(self, amt):
        obj[self.user].deposit(amt)

    def block(self):
        obj[self.user].blocked = True



obj = []
obj.append(Bank("Manu Ayala", "56789", "1234", 10000, 500))
obj.append(Bank("Isaac Asimov", "112233445", "1007", 800, 350))


if __name__ == "__main__":

    atm = Machine(None, 10000)
    while True:
        atm.user = None
        print("\n\n\n-----------------------")
        print "Insert card / Enter name and card number"
        print("-----------------------\n")
        name = raw_input("Name: ")
        num = raw_input("Card number: ")

        card_found = atm.card(name, num)

        if card_found == "Blocked":
            print("Card is Blocked")

        elif card_found:
            i = 3
            print("-----------------------")
            print "Enter PIN number"
            print("-----------------------\n")
            while i>0:

                pin_entered = raw_input()

                if atm.check_pin(pin_entered) != "denied":
                    print("-----------------------")
                    acc = raw_input("Select account--> Savings(S) or checking(C): ")
                    while acc != 'S' and acc!='C':
                        acc = raw_input("Select account--> Savings(S) or checking(C): ")
                        print("Wrong entery, try again")
                    atm.set_acc(acc)

                    print("-----------------------\n")
                    print("(1) Check balance")
                    print("(2) Withdraw")
                    print("(3) Deposit")
                    print("Enter 1,2 or 3")
                    print("-----------------------\n")
                    action = raw_input()
                    while action!="1" and action!="2" and action!="3":
                        action = raw_input()
                        print("Enter value again")
                    if "1"==action:
                        atm.display()
                    elif "2"==action:
                        amount = raw_input("Enter amount to withdraw")
                        atm.withdraw(amount)
                    elif "3"==action:
                        amount = raw_input("Enter amount to deposit")
                        atm.deposit(amount)
                    print("Thank you!")
                    break
                else:
                    print("Wrong PIN: try " + str(i) + " more time(s)")
                    i = i-1

                if i == 0:
                    print("Card blocked, too many tries")
                    atm.block()

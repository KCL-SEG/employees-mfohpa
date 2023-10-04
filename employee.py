"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salOrWage, hours = 0, bonus = 0, contComm = 0, contractNo = 0):
        self.name = name
        self.hours = hours
        self.salOrWage = salOrWage
        self.bonus = bonus
        self.contComm = contComm
        self.contractNo = contractNo

    def base(self):
        if self.hours:
            return self.salOrWage * self.hours
        else:
            return self.salOrWage

    def commission(self):
        if self.bonus:
            return self.bonus
        elif self.contComm:
            return self.contComm * self.contractNo
        else:
            return 0
        
    def get_pay(self):
        return self.base() + self.commission()

    def monthlyOrContract(self):
        if self.hours:
            return f"contract of {self.hours} hours at {self.salOrWage}/hour"
        else:
            return f"monthly salary of {self.salOrWage}"

    def commissionStatement(self):
        if self.bonus:
            return f" and receives a bonus commission of {self.bonus}"
        elif self.contComm:
            return f" and receives a commission for {self.contractNo} contract(s) at {self.contComm}/contract"
        else:
            return ""

    def __str__(self):
        return f"{self.name} works on a {self.monthlyOrContract()}{self.commissionStatement()}. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee("Billie", 4000)
print(billie.get_pay())
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee("Charlie", 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee("Renee", 3000, contractNo=4, contComm=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee("Jan", 25, 150, contractNo=3, contComm=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee("Robbie", 2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee("Ariel", 30, 120, bonus=600)

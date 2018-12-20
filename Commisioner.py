
#This class allows for editing creation of comisioner's info
class Commisioner:

    def __init__(self, name, price, email):
        self.name = name
        self.price = price
        self.email = email

    def getName(self):
        return self.name

    def setName(self,n):
        self.name = n

    def getPrice(self):
        return self.price

    def setPrice(self,s):
        self.price = s

    def getEmail(self):
        return self.email
    
    def setEmail(self,e):
        self.email = e
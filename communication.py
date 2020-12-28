class communication():

    def __init__(self, letter, keyy ):
        self.message = letter
        self.key = keyy
        self.kkey = "qonpacfrhsbivmtluzjewkygxd"
        self.symbols = ["," , ".", " ", "?", "(", ")", "\"", "\'", ";", ":"]
        self.result = ""



    def encrypt(self):
        for i in self.message[0:]:
            if i.isupper():
                key = self.kkey.upper()
                position = self.kkey.find(i)
                value = position + self.key
                if value > 25:
                    value = (value - 26)
                self.result += self.kkey[value]

            elif i.islower():
                position = self.kkey.find(i)
                value = position + self.key
                if value > 25:
                    value = (value - 26)
                self.result += self.kkey[value]
            elif i in self.symbols:
                self.result += i
        print(self.result)


    def decrypt(self):
        for i in self.message[0:]:
            if i.isupper():
                key = self.kkey.upper()
                position = self.kkey.find(i)
                value = position - self.key
                if position < self.key:
                    if self.key % 2 != 0:
                        if position == (self.key//2) + 1:
                            value = 26 - (self.key - position)
                else:
                    value = position - self.key
                self.result += self.kkey[value]

            elif i.islower():
                position = self.kkey.find(i)
                value = position - self.key
                if position < self.key:
                    if self.key % 2 != 0:
                        if position == (self.key//2) :
                            value = 26 - (self.key - position)
                else:
                    value = position - self.key
                self.result += self.kkey[value]
            elif i in self.symbols:
                self.result += i
        print(self.result)



message = input("Copy and paste the file without any edit here :")
key = int(input("Enter the key for decription :"))
obj = communication(message, key)

s = input("Do you want to read or write the file :")

if s in ["read", "r"]:
    obj.decrypt()
elif s in ["write", "w"]:
    obj.encrypt()
else:
    print("Enter 'read/r' or 'write/w' for acces this code")

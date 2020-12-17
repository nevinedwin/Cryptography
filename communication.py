class communication():
    def encrypt(self, letter, val):
        result = ""
        for i in letter[0:]:
            key = "qonpacfrhsbivmtluzjewkygxd"
            if i.isupper():
                key = key.upper()
                position = key.find(i)
                value = position + val
                if value > 25:
                    value = (value - 26)
                result += key[value]

            elif i.islower():
                position = key.find(i)
                value = position + val
                if value > 25:
                    value = (value - 26)
                result += key[value]
            elif i in ["," , ".", " ", "?", "(", ")", "\"", "\'", ";", ":"]:
                result += i
        print(result)


    def decrypt(self, letter, val):
        result = ""
        for i in letter[0:]:
            key = "qonpacfrhsbivmtluzjewkygxd"
            if i.isupper():
                key = key.upper()
                position = key.find(i)
                value = position - val
                if position < val:
                    if val % 2 != 0:
                        if position == (val//2) + 1:
                            value = 26 - (val - position)
                else:
                    value = position - val
                result += key[value]

            elif i.islower():
                position = key.find(i)
                value = position - val
                if position < val:
                    if val % 2 != 0:
                        if position == (val//2) :
                            value = 26 - (val - position)
                else:
                    value = position - val
                result += key[value]
            elif i in ["," , ".", " ", "?", "(", ")", "\"", "\'", ";", ":"]:
                result += i
        print(result)






obj = communication()

s = input("Do you want to read or write the file :")

if s in ["Read", "read", "READ", "r", "R"]:
    message = input("Copy and paste the file without any edit here :")
    key = int(input("Enter the key for decription :"))
    obj.decrypt(message, key)
elif s in ["Write", "write", "w", "W", "WRITE"]:
    message = input("Type here (dont use emoji's) :")
    key = int(input("Enter the encryption key :"))
    obj.encrypt(message, key)
else:
    print("Enter 'read/r' or 'write/w' for acces this code")

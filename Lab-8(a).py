class PaliStr:
    def __init__(self):
        self.isPali=False
    def isPalindrom(self,mystr):
        if mystr==mystr[::-1]:
            self.isPali=True
        else:
            self.isPali=False
        return self.isPali
class PaliInt(PaliStr):
    def __init__(self):
        self.isPali=False
    def isPalindrom(self,myInt):
        temp=myInt
        rev=0
        while temp!=0:
            dig=temp%10
            rev=(rev*10)+dig
            temp=temp//10
        if myInt==rev:
            self.isPali=True
        else:
            self.isPali=False
        return self.isPali
mystr=input("Enter a string:")
obj=PaliStr()
if obj.isPalindrom(mystr):
    print("Palindrome:")
else:
    print("NOT")
val=int(input("Enter a string:"))
obj1=PaliInt()
if obj1.isPalindrom(val):
    print("Palindrome:")
else:
    print("NOT")
    
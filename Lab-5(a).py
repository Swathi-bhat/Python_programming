import re

def isphno(num_str):
    if len(num_str)!=12:
        return False
    for i in range(len(num_str)):
        if i==3 or i==7:
            if num_str[i]!="-":
                return False
        else:
            if num_str[i].isdigit()==False:
                return False
    return True
def chkhphno(num_str):
    pattern=re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if pattern.match(num_str):
        return True
    else:
        return False
    
num_str=input("Enter Phone number:")
print("Without regular expression")
if isphno(num_str):
    print("Valid")
else:
    print("Not valid")
print("Using regular expression")
if chkhphno(num_str):
    print("Valid")
else:
    print("Not valid")

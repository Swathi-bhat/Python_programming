val=input("Enter a string:")
rev=val[::-1]

if rev==val:
    print("Palindrome")
else:
    print("Not a palindrome")
for i in range(10):
    if rev.count(str(i))>0:
        print(str(i)," appears ",rev.count(str(i))," times")
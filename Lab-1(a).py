m1=int(input("Enter the marks for test 1:"))
m2=int(input("Enter the marks for test 2:"))
m3=int(input("Enter the marks for test 3:"))
if m1<=m2 and m1<=m3:
     marks=(m2+m3)/2
elif m2<=m1 and m2<=m3:
    marks=(m1+m3)/2
else:
    marks=(m1+m2)/2
print("average marks:",marks)

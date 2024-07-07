import os.path
import sys
fname=input("Enter file name:")
if not os.path.isfile(fname):
    print("No such file")
    sys.exit(0)
infile=open(fname,"r")
lineList=infile.readlines()
for i in range(5):
    print(i+1,":",lineList[i])
word=input("enter a word:")
cnt=0
for line in lineList:
    cnt+=line.count(word)
print("The word appears:",cnt)
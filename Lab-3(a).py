sentence=input("Enter a sentence:")
wordCnt=sentence.split(" ")
print("Words:",len(wordCnt))
dig=up=down=0
for ch in sentence:
    if '0'<=ch<='9':
        dig+=1
    elif 'a'<=ch<='z':
        down+=1
    elif 'A'<=ch<='Z':
        up+=1
print("Digits:",dig," uppercase:",up," lowercase:",down)
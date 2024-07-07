import random

def mergeSor(lst):
    if len(lst)>1:
        mid = len(lst)//2
        left_half=lst[:mid]
        right_half=lst[mid:]
        mergeSor(left_half)
        mergeSor(right_half)
        i=j=k=0
        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                lst[k]=left_half[i]
                i+=1
            else:
                lst[k]=right_half[j]
                j+=1
            k+=1
        while i<len(left_half):
            lst[k]=left_half[i]
            i+=1
            k+=1
        while j<len(right_half):
            lst[k]=right_half[j]
            j+=1
            k+=1
    return lst
def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
my_list=[]
for i in range(10):
    my_list.append(random.randint(0,999))
print("Unsorted array")
print(my_list)
print("Insertion sort")
insertionSort(my_list)
print(my_list)
my_list=[]
for i in range(10):
    my_list.append(random.randint(0,999))
print("Unsorted array")
print(my_list)
print("Mergesort")
mergeSor(my_list)
print(my_list)
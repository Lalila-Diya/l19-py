list=[10,23,42,4,8,45]
print("List :", list)
sum=0
for i in list:
    sum=sum+i

print("Sum of list: ",sum)
avg=sum/len(list)
print("Average of list: ",avg)

#sort list
list.sort()
print("Smallest No.: ",list[0])
print("Longest No.: ",list[-1])
print("Sorted List: ",list)
print("Recersed list: ",list[::-1])
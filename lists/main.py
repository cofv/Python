"""
list1 = ["he","P","D"]
list2 = []

for ord in list1:
    print(ord)

for i in range(len(list1)):
    print(list1(i))

for ord in list1:
    list2.append(ord + "!")

print(list2)

list1 = input().split()
list2 = []


for i in range(len(list1)):
    list2.append(len(list1[i]))

print(list2)
"""

list1 = ["He","p","d"]
list2 = ["j","å","ig"]
list3 = []
#1 + 1, 2 + 2, 3 + 3.

for i in range(len(list1)):
    #print(list1[i] + list2[i])
    list3.append(list1[i] + list2[i])
print(list3)




numlist = [10,2,4,5,5,5,3,2, "a"]

print("This is thy list auf numbers" + str(numlist))

user_input = input("Type which number you want to remove ")

try:
    user_input = int(user_input)
except:
    pass
"""
numba = (numlist.count(user_input))
"""
while user_input in numlist:
    numlist.pop(numlist.index(user_input))

print("I have removed ye number " + str(numlist))
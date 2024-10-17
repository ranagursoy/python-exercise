# Description: Write a Python program to combine two lists and remove duplicates.

list1 = [1, 2, 2, 3, 4]
list2 = [3, 4, 4, 5, 6]

# Solution 1

def combinate_lists(list1, list2):
    return list(set(list1 + list2))

print("************************** Solution 1 **************************")
print(combinate_lists(list1, list2))

# Solution 2
def combinate_lists(list1, list2):
    return list(dict.fromkeys(list1 + list2))

print("************************** Solution 2 **************************")
print(combinate_lists(list1, list2))
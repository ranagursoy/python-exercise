# Description: Find the most frequent element in an array

list1 = [1, 2, 2, 3, 4]

def most_freq_element(list1):
    if not list1:
        return None  
    
    list1 = sorted(list1)  
    max_count = 1
    count = 1
    element = list1[0]  

    for i in range(1, len(list1)):  
        if list1[i] == list1[i - 1]: 
            count += 1
        else:
            count = 1  

        if count > max_count:  
            max_count = count
            element = list1[i]

    return element 

print("************************** Solution 1 **************************")
print(most_freq_element(list1))

# Solution 2

def most_freq_element(list1):
    return max(set(list1), key = list1.count)

print("************************** Solution 2 **************************")
print(most_freq_element(list1))
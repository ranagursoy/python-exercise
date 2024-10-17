# Consecutive Sequence
# Given a list of integers, return the length of the longest consecutive sequence.

input_array1 = [100, 4, 200, 1, 3, 2]
input_array2 = []
input_array3 = [10]
input_array4 = [5, 10, 15, 20]
input_array5 = [1, 1, 2, 2, 3, 3]

# Solution 1

def consecutive_sequence(input_array):
    output = []
    count = 1
    input_array = sorted(set(input_array))

    if not input_array:
        return 0

    for i in input_array:
        if i + 1 in input_array:
            count += 1
        else:
            count = 1
        output.append(count)

    return max(output) 
  
print("************************** Solution 1 **************************")
print(consecutive_sequence(input_array1))

# Solution 2

def consecutive_sequence(input_array):
    if not input_array:
        return 0  
    
    input_array = sorted(set(input_array))  
    longest = 1  
    count = 1  

    for i in range(1, len(input_array)):
        if input_array[i] == input_array[i - 1] + 1: 
            count += 1
        else:
            longest = max(longest, count) 
            count = 1  

    return max(longest, count)

print("************************** Solution 2 **************************")
print(consecutive_sequence(input_array1))

# Solution 3

def consecutive_sequence_advanced(input_array):
    if not input_array:  
        return 0
    
    num_set = set(input_array)  
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

print("************************** Solution 3 **************************")
print(consecutive_sequence_advanced(input_array1))

# Solution 4

def consecutive_sequence(nums):
    num_set = set(nums)
    return max((len({x + i for i in range(len(nums))} & num_set) for x in num_set), default=0)

print("************************** Solution 4 **************************")
print(consecutive_sequence(input_array1))
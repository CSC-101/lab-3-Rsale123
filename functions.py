# Double the value of a number.
def double(n: int) -> int:
    doubled_value = n * 2  # Renamed to avoid shadowing 'result'
    return doubled_value


# Task 1 - List Comprehensions

# List comprehension example: adding 1 to each element in the list.
more = [x + 1 for x in [1, 2, 3, 4]]
print(more)

# Using the square function in list comprehension.
def square(n: int) -> int:
    return n * n

squares = [square(x) for x in [1, 2, 3, 4]]
print(squares)

# Using check function in list comprehension.
def check(n: int) -> bool:
    return n > 2

answer = [x for x in range(5) if check(x)]
print(answer)

# Using inc function in list comprehension.
def inc(m: int) -> int:
    return m + 1

answer = [inc(x) for x in range(5) if check(x)]
print(answer)


# Task 2 - Loops

# Tally the sum of all elements in a list.
def tally(nums: list[int]) -> int:
    total_sum = 0  # Renamed to avoid shadowing 'result'
    for num in nums:  # Loop through each element in the list.
        total_sum = total_sum + num
    return total_sum

tally_result = tally([4, 9, 2, 1])
print(tally_result)

# Copy a list by appending each element using a loop.
def copy(nums: list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):  # Loop through the list by index.
        new_list.append(nums[idx])
    return new_list

copy_result = copy([4, 9, 2, 1])
print(copy_result)

# Increment all elements in the list by 1 using a loop.
def increment_all(nums: list[int]) -> list[int]:
    new_list = []
    for value in nums:  # Loop through the list by value.
        new_list.append(value + 1)
    return new_list

incremented_list = increment_all([4, 9, 2, 1])
print(incremented_list)


# Task 3 - Test Cases

# Function to group a list into sublists of 3 elements
def groups_of_3(lst):
    return [lst[i:i+3] for i in range(0, len(lst), 3)]


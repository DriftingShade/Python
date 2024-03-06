# 1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, 
# from the number (as the 0th element) down to 0 (as the last element).
arr = []
def num_Countdown(num):
    for i in range(num, -1, -1):
        arr.append(i)
    return arr
print(num_Countdown(10))


# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
num_list = [5,3]
def print_and_return(num_list):
    print(num_list[0])
    return num_list[1]
x = print_and_return(num_list)
print(x)


# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
list2 = [1,2,3,4,5]
def first_plus_length(list2):
    sum = list2[0] + len(list2)
    return sum
x = first_plus_length(list2)
print(x)


# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original
#  list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
arr1 = [5,2,3,2,1,4]
arr2 = [3]
def values_greater_than_second(arr):
    newarr = []
    sum = 0
    for i in arr:
        if len(arr) < 2:
            print(False)
            break
        elif i > arr[1]:
            newarr.append(i)
            sum += 1
    print(sum)
    return newarr
print(values_greater_than_second(arr1))
print(values_greater_than_second(arr2))


# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value.
#  The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def length_and_value(size,value):
    return [value] * size
print(length_and_value(4,7))
print(length_and_value(6,2))
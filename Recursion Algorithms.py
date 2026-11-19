# Merge Sort:
list1 = [3, 5, 6, 1, 2]
list2 = [1, 6, 2, 4]
list3 = [1, 20, 19, 7, 18, 6, 15, 2]
def merge(list1, list2):
    result = []
    i = 0
    j = 0
    while i<len(list1) and j<len(list2):
        if list1[i]<list2[j]:
            result.append(list1[i])
            i+=1
        else:
            result.append(list2[j])
            j+=1
    return result + list1[i:] + list2[j:]

def merge_sort(list):
    if len(list)<=1:
        return list
    mid = len(list)//2
    left_sorted = merge_sort(list[:mid])
    right_sorted = merge_sort(list[mid:])
    return merge(left_sorted, right_sorted)

print(merge_sort(list3))

# Factorial calculation:
def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n
print (factorial(4))

# Binary Search with recursion:
def recbinary_search(left, right, readings: list, target: int) -> tuple:
    if left>right:
        return -1
    mid = (left+right)//2
    if readings[mid]>target:
        return recbinary_search(left, mid-1, readings, target)
    elif readings[mid]<target:
        return recbinary_search(mid+1, right, readings, target)
    else:
        return (mid, readings[mid])
list4 = sorted(list3)
print(recbinary_search(0, len(list4)-1, list4, 7))

#  Fibonnaci nth number
def fib(n: int)->int:
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(10))

# Unpacking Childs
cargo = [[1,2,3], [1,3], 2, 3, [4]]
def cargo_sum(list):
    total =  0
    for item in list:
        if isinstance(item, int):
            total+=item
        else:
            total+=cargo_sum(item)
    return total

print (cargo_sum(cargo))


# Palindromes:
def is_palindrome(string):
    left = 0
    right = len(string)-1
    if len(string) <= 1:
        return True
    elif string[left] == string[right]:
        substr = string[left+1:right]
        # or write
        # substr = string[1:-1]
        return is_palindrome(substr)
    else:
        return False

print(is_palindrome("abba"))
print(is_palindrome("abca"))


# Assignment 3 Q2:
# Using Recursive Binary Search, find in a string the starting and ending position of value = target:
search = [1,2,3,4,4,4,4,5,6]
def rec_binary_bound(list, target, left, right):
    # finding lower bound
    def lower_bound(left, right):
        if left>right:
            return -1
        mid = (left+right)//2
        if list[mid]>target:
            return lower_bound(left, mid-1)
        elif list[mid]<target:
            return lower_bound(mid+1, right)
        else:
            earlier = lower_bound(left, mid-1)
            if earlier == -1:
                return mid
            else:
                return earlier

        # finding upper bound
    def upper_bound(left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if list[mid] > target:
            return upper_bound(left, mid - 1)
        elif list[mid] < target:
            return upper_bound(mid + 1, right)
        else:
            earlier = upper_bound(mid+1, right)
            if earlier == -1:
                return mid
            else:
                return earlier

    return (lower_bound(left, right), upper_bound(left, right))

print(rec_binary_bound(search, 4, 0, len(search)-1))



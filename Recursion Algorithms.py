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
def recbinary_search(left, right, readings: list, target: int) -> int:
    if left>right:
        return -1
    mid = (left+right)//2
    if readings[mid]>target:
        return recbinary_search(left, mid-1, readings, target)
    elif readings[mid]<target:
        return recbinary_search(mid+1, right, readings, target)
    else:
        return [mid, readings[mid]]
list4 = sorted(list3)
print(recbinary_search(0, len(list4)-1, list4, 7))






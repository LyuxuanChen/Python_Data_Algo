unsorted1 = [7, 6, 4, 10, 3, 2, 3]
unsorted2 = [7, 6, 4, 10, 3, 2, 3]
unsorted3 = [7, 6, 4, 10, 3, 2, 3]

def bubble_sort(arr: list) -> None:
    size = len(arr)

    for i in range(size-1):
        swap_count = 0
        for j in range (size-1):
            if arr[j]>arr[j+1]:
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp
                swap_count+=1
        if swap_count == 0:
            break

def insertion_sort(arr: list) -> None:
    size  = len(arr)
    for i in range (1, size):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

def selection_sort(arr: list) ->None:
    size = len(arr)
    for i in range (size):
        minimum = i
        for j in range (i+1, size):
            if arr[j]<arr[minimum]:
                minimum = j
        if minimum!=i:
            tmp = arr[i]
            arr[i] = arr[minimum]
            arr[minimum] = tmp

bubble_sort(unsorted1)
insertion_sort(unsorted2)
# selection_sort(unsorted3)
print (unsorted1)
print(unsorted2)
print(unsorted3)


# bubble sort
# for j  in range (size-1):
#     for i in range (0, size-1):
#         if unsorted[i]>unsorted[i+1]:
#             tmp = unsorted[i]
#             unsorted[i] = unsorted[i+1]
#             unsorted[i+1] = tmp
#
# print(unsorted)

# insertion sort:
# for i in range (1, size):
#     target = unsorted[i]
#     j = i-1
#     while j>=0 and unsorted[j]>target:
#         unsorted[j+1] = unsorted[j]
#         j-=1
#     unsorted[j+1] = target
#
# print(unsorted)

# # selection sort:
# for start in range (size-1):
#     minimum = start
#     for j in range (start+1, size):
#        if unsorted[j]<unsorted[minimum]:
#            minimum = j
#     if minimum!=start:
#         tmp = unsorted[start]
#         unsorted[start] = unsorted[minimum]
#         unsorted[minimum] = tmp
# print (unsorted)
#



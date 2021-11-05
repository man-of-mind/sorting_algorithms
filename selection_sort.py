def selection_sort(array: list):
    for i in range(len(array) - 1):
        val = array[i]
        pos_mini = i
        for j in range((i + 1), len(array)):
            if array[j] < array[pos_mini]:
                pos_mini = j
        array[i], array[pos_mini] = array[pos_mini], val

    return array


def bubble_sort(array: list):
    for k in range(1, len(array)):
        swapped = False
        for i in range(0, (len(array) - k)):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = 1
        if swapped == True:
            break

    return array


def insertion_sort(array: list):
    for i in range(1, len(array)):
        value = array[i]
        hole = i
        while(hole > 0 and array[hole - 1] > value):
            array[hole] = array[hole - 1]
            hole -= 1

        array[hole] = value
 
    return array

def merge_sort(array: list):
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while (i < len(left) and j < len(right)):
            if left[i] > right[j]:
                array[k] = right[j]
                j+=1
            else:
                array[k] = left[i]
                i+=1
            k+=1


        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
  
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


def quick_sort(array: list, start: int, end: int):
    if start < end:
        pivot_index = partition(array, start, end)
        quick_sort(array, start, pivot_index - 1)
        quick_sort(array, pivot_index + 1, end)


def partition(array: list, start: int, end: int):
    pivot = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] < pivot:
            i+= 1
            array[i] = array[j]
    array[i + 1] = pivot
    return i + 1


print(selection_sort([7,1,2,5,3,6,1,8,4]))
print(bubble_sort([1,2,5,7,3,6,1,8,4]))
print(insertion_sort([1,2,5,3,7,6,1,8,4]))
array = [1,2,5,3,7,6,1,8,4]
merge_sort(array=array)
print(array)
quick_sort(array=array, start=0, end=8)
print(array)


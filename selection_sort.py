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
        flag = 0
        for i in range(0, (len(array) - k)):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                flag = 1
        if flag == 0:
            break

    return array


print(selection_sort([1,2,5,3,6,1,8,4]))
print(bubble_sort([1,2,5,3,6,1,8,4]))
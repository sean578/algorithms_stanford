def quicksort(array, pivot_index):
    """ Sort data, low to high using quicksort method """
    if len(array) <= 1:
        return array

    pivot = array[pivot_index]
    array, new_pivot_index = partition(array, 0)

    array_left = quicksort(array[:new_pivot_index], 0)
    array_right = quicksort(array[new_pivot_index+1:], 0)

    # concatenate
    array = array_left + [pivot] + array_right

    # return the sorted array & the number of comparisons made
    return array


def partition(array, pivot_index=0):
    """ perform partition around pivot """

    # choose the pivot
    pivot = array[pivot_index]

    # i, j used to loop through & do comparisons
    i = pivot_index + 1  # just right of pivot
    for j in range(pivot_index + 1, len(array)):
        if array[j] < pivot:
            # swap array[i] & array[j]
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i += 1

    # swap pivot into correct position
    array[pivot_index] = array[i-1]
    array[i-1] = pivot

    # return the ordered array and the pivot index
    return array, i-1


if __name__ == '__main__':
    filepath = './data/assignment_3.txt'
    data = []
    for line in open(filepath).readlines():
        data.append(int(line.strip('\n')))

    array = quicksort(data, 0)
    print('array', array)
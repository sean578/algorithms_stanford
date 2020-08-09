def quicksort(array, comparisons):
    """ Sort data, low to high using quicksort method """

    if len(array) <= 1:
        return array, comparisons

    pivot = array[0]
    array, new_pivot_index = partition(array, 0)

    # recurse left of pivot
    comparisons += len(array[:new_pivot_index]) - 1
    array_left, comparisons = quicksort(array[:new_pivot_index],
                                        comparisons)
    # recurse right of pivot
    comparisons += len(array[new_pivot_index+1:]) - 1
    array_right, comparisons = quicksort(array[new_pivot_index+1:],
                                             comparisons)

    # concatenate
    array = array_left + [pivot] + array_right

    # return the sorted array & the number of comparisons made
    # print('comparison in quicksort', comparisons)
    return array, comparisons


def partition(array, pivot_index):
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
    array[0] = array[i-1]
    array[i-1] = pivot

    # return the ordered array and the pivot index
    return array, i-1


if __name__ == '__main__':
    filepath = './data/assignment_3.txt'
    data = []
    for line in open(filepath).readlines():
        data.append(int(line.strip('\n')))

    to_show = 5

    comparisons = 0
    array, comparisons = quicksort(data, comparisons)

    print('array start: {}\narray finish: {}\n'.format(array[:to_show],
                                                       array[-to_show:]))
    print('comparisons in main', comparisons)

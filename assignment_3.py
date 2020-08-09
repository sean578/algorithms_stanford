def quicksort(array, comparisons, pivot_index):
    """ Sort data, low to high using quicksort method """

    if len(array) <= 1:
        return array, comparisons

    pivot = array[pivot_index]

    array = swap_pivot_into_first_index(array, pivot, pivot_index)
    left_bucket, right_bucket = partition(array)

    # recurse left of pivot
    comparisons += len(left_bucket) - 1
    ordered_array_left, comparisons = quicksort(left_bucket,
                                        comparisons,
                                        pivot_index)
    # recurse right of pivot
    comparisons += len(right_bucket) - 1
    ordered_array_right, comparisons = quicksort(right_bucket,
                                         comparisons,
                                         pivot_index)

    # concatenate
    array = ordered_array_left + [pivot] + ordered_array_right

    # return the sorted array & the number of comparisons made
    # print('comparison in quicksort', comparisons)
    return array, comparisons


def swap_pivot_into_first_index(array, pivot, pivot_index):
    # swap pivot into position 0
    array[pivot_index] = array[0]
    array[0] = pivot
    return array


def partition(array):
    """ perform partition around pivot """

    # choose the pivot
    pivot = array[0]

    # i, j used to loop through & do comparisons
    i = 1  # just right of pivot
    for j in range(1, len(array)):
        if array[j] < pivot:
            # swap array[i] & array[j]
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i += 1

    # swap pivot into correct position
    array[0] = array[i-1]
    array[i-1] = pivot

    # return two arrays, one each side of pivot
    return array[:i-1], array[i:]


if __name__ == '__main__':
    filepath = './data/assignment_3.txt'
    data = []
    for line in open(filepath).readlines():
        data.append(int(line.strip('\n')))

    to_show = 5
    pivot_index = -1

    comparisons = 0
    array, comparisons = quicksort(data, comparisons, pivot_index)

    print('array start: {}\narray finish: {}\n'.format(array[:to_show],
                                                       array[-to_show:]))
    print('comparisons in main', comparisons)

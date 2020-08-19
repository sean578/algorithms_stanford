from random import randrange


def quicksort(array, comparisons, pivot_index):
    """ Sort data, low to high using quicksort method """

    if len(array) <= 1:
        return array, comparisons

    pivot = array[pivot_index]

    array = swap_pivot_into_first_index(array, pivot, pivot_index)
    left_bucket, right_bucket = partition(array)

    # recurse left of pivot
    comparisons += len(left_bucket) - 1
    pivot_left = median_of_three_pivot(left_bucket)
    ordered_array_left, comparisons = quicksort(left_bucket,
                                        comparisons,
                                        pivot_left)
    # recurse right of pivot
    comparisons += len(right_bucket) - 1
    pivot_right = median_of_three_pivot(right_bucket)
    ordered_array_right, comparisons = quicksort(right_bucket,
                                         comparisons,
                                         pivot_right)

    # concatenate
    array = ordered_array_left + [pivot] + ordered_array_right

    # return the sorted array & the number of comparisons made
    # print('comparison in quicksort', comparisons)
    return array, comparisons


def random_pivot(array):
    if len(array) > 0:
        return randrange(len(array))
    else:
        return 0


def median_of_three_pivot(array):
    if len(array) < 3:
        return 0
    else:
        l, m, r = [array[0], array[len(array)//2], array[-1]]  # l, m, r
        if l < m:
            if l > r:
                return 0
            elif r > m:
                return len(array)//2
            else:
                return -1
        else:
            if m > r:
                return len(array)//2
            elif r < l:
                return -1
            else:
                return 0


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
    filepath = 'data/course_1_assignment_3.txt'
    data = []
    for line in open(filepath).readlines():
        data.append(int(line.strip('\n')))

    pivot_index_initial = randrange(len(data))

    comparisons = 0
    array, comparisons = quicksort(data, comparisons, pivot_index_initial)

    to_show = 5
    print('array start: {}\narray finish: {}\n'.format(array[:to_show],
                                                       array[-to_show:]))
    print('comparisons in main', comparisons)

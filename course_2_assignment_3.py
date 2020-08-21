""" Median Maintenance algorithm.
Calculate the median on the stream of numbers - find the sum of the medians
"""

import heapq


def load_nums(filehandle):
    nums = []
    for line in filehandle.readlines():
        nums.append(int(line.strip('\n')))
    return nums


def median_maintainence(nums):

    # create separate extract max and extract min heaps
    heap_HIGH = []
    heap_LOW = []

    # keep track of number of entries in each heap
    num_in_high = 0
    num_in_low = 0

    medians = []
    for i, num in enumerate(nums):
        if i == 0:
            heapq.heappush(heap_LOW, -1*num)
            num_in_low += 1
        elif num < -1*heap_LOW[0]:
            heapq.heappush(heap_LOW, -1*num)
            num_in_low += 1
            if num_in_low > num_in_high + 1:
                max_of_low = -1*heapq.heappop(heap_LOW)
                heapq.heappush(heap_HIGH, max_of_low)
                num_in_low -= 1
                num_in_high += 1
        else:
            heapq.heappush(heap_HIGH, num)
            num_in_high += 1
            if num_in_high > num_in_low:
                min_of_high = heapq.heappop(heap_HIGH)
                heapq.heappush(heap_LOW, -1*min_of_high)
                num_in_high -= 1
                num_in_low += 1

        median = -1*heap_LOW[0]
        medians.append(median)

    return medians


if __name__ == '__main__':
    filehandle = open('data/course_2_assignment_3.txt')
    nums = load_nums(filehandle)

    medians = median_maintainence(nums)
    print('sum of medians =', sum(medians))
    print('sum of medians % 10000 =', sum(medians) % 10000)

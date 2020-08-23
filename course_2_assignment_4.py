def load_nums(filehandle):
    nums = set()
    for line in filehandle.readlines():
        nums.add(int(line.strip('\n')))
    return nums


if __name__ == '__main__':
    filehandle = open('data/course_2_assignment_4.txt')
    nums = load_nums(filehandle)
    print(type(nums))

    nums_list = sorted(list(nums))

    # for each value check if the required value exists
    # look for required value - x

    found = 0

    # for t in list(range(3, 10 + 1)):
    for t in list(range(-10000, 10000 + 1)):
        print(t)
        for num in nums_list:
            if t - num in nums:
                # check numbers are distinct
                if num != t-num:
                    print('ok')
                    found += 1
                    break
    print('total found', found)
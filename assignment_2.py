def count_inversions_and_sort(a):
    # if only one elements left then no inversions and already sorted
    if len(a) <= 1:
            return 0, a  # a already sorted
    else:
        # split array
        b, c = a[:len(a)//2], a[len(a)//2:]

        # print('b, c', b, c)

        # count inversions in each half
        inversion_count_b, x = count_inversions_and_sort(b)
        inversion_count_c, y = count_inversions_and_sort(c)

        # sort the arrays
        x.sort()
        y.sort()

        # count the split inversions
        inversion_count_split, z = count_split_inversions(x, y)

        # sum up all the inversions
        # print(inversion_count_b, inversion_count_c, inversion_count_split)
        total_inversions = inversion_count_b + inversion_count_c + inversion_count_split

        return total_inversions, z


def count_split_inversions(b, c):
    i = 0
    j = 0
    z = []
    inversions = 0

    while i < len(b) or j < len(c):
        # print(b, c, i, j, inversions)

        if i == len(b):
            z.append(c[j])
            j += 1
        elif j == len(c):
            z.append(b[i])
            i += 1
        elif b[i] < c[j]:
            z.append(b[i])
            i += 1
        elif b[i] > c[j]:
            z.append(c[j])
            inversions += len(b) - i
            j += 1

    return inversions, z


if __name__ == '__main__':

    a = []
    for line in open('./data/assignment_2.txt').readlines():
        a.append(int(line.strip()))

    print(count_inversions_and_sort(a)[0])
    # print(count_inversions_and_sort(a)[1])
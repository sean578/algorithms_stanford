"""
implement one or more of the integer multiplication algorithms described in lecture.
Your program should restrict itself to multiplying only pairs of single-digit numbers.
Implement recursive integer multiplication and/or Karatsuba's algorithm.
What's the product of the following two 64-digit numbers?
3141592653589793238462643383279502884197169399375105820974944592
2718281828459045235360287471352662497757247093699959574966967627
the number of digits in each input number is a power of 2
"""

"""
Karatsuba's algorithm
x*y = [a, b]*[c, d]
a = 1st half x
b = 2nd half x
c = 1st half y
d = 2nd half y

a1 = a*c
a2 = b*c
a3 = (a+b)(c+d)

a4 = a3-a2-a1
x*y = (a1 << 4) + (a2) + (a4 << 2)
"""


def karatsuba(x, y):

    x_string = str(x)
    y_string = str(y)

    lx = len(x_string)
    ly = len(y_string)

    # if len(x) and len(y) are 1 then return mult
    if lx == 1 and ly == 1:
        return x*y

    l = max(lx, ly)
    l2 = l // 2

    # split x & y in half
    a, b = x // 10**l2, x % 10**l2
    c, d = y // 10**l2, y % 10**l2

    # do 3 recursive calls for the products
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    a_b_c_d = karatsuba(a+b, c+d)

    ad_bc = a_b_c_d - ac - bd

    return (ac*10**(2*l2)) + bd + (ad_bc*10**l2)


if __name__ == '__main__':
    # assumes num digits in both x and y are equal and a power of 2
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627

    x_y = karatsuba(x, y)
    print(x_y)

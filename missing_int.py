'''
Given an array of integers, find the first missing positive integer in linear time and
constant space. In other words, find the lowest positive integer that does not exist
in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
'''


def missing_positive_integer(list_num):
    set_num = set([x for x in list_num if x>0])
    k = 1
    while True:
        if k in set_num:
            k = k+1
        else:
            break
    return k


if __name__ == "__main__":
    import time
    ll = [3, 2, 5, -1, 1]

    t0 = time.time()
    print(missing_positive_integer(ll))
    print(time.time()-t0)

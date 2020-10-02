'''
Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''


def product_array(list_num):
    output = []
    total = 1
    for n in list_num:
        total *= n

    for n in list_num:
        output.append(int(total/n))

    return output


def other_soln_one(arr, n): # https://www.geeksforgeeks.org/a-product-array-puzzle/
    # Allocate memory for temporary arrays left[] and right[]
    left = [0] * n
    right = [0] * n

    # Allocate memory for the product array
    prod = [0] * n

    # Left most element of left array is always 1
    left[0] = 1

    # Rightmost most element of right array is always 1
    right[n - 1] = 1

    # Construct the left array
    for i in range(1, n):
        left[i] = arr[i - 1] * left[i - 1]

        # Construct the right array
    for j in range(n - 2, -1, -1):
        right[j] = arr[j + 1] * right[j + 1]

        # Construct the product array using
    # left[] and right[]
    for i in range(n):
        prod[i] = left[i] * right[i]

    return prod
    # print the constructed prod array
    # output
    # for i in range(n):
    #     print(prod[i], end=' ')


def other_soln_two(arr, n):

    i, temp = 1, 1

    # Allocate memory for the product array
    prod = [1 for i in range(n)]

    # Initialize the product array as 1

    # In this loop, temp variable contains product of
    # elements on left side excluding arr[i]
    for i in range(n):
        prod[i] = temp
        temp *= arr[i]

    # Initialize temp to 1 for product on right side
    temp = 1

    # In this loop, temp variable contains product of
    # elements on right side excluding arr[i]
    for i in range(n - 1, -1, -1):
        prod[i] *= temp
        temp *= arr[i]

    return prod

    # # Print the constructed prod array
    # for i in range(n):
    #     print(prod[i], end=" ")
    #
    # return


if __name__ == "__main__":
    arr = [10, 3, 5, 6, 2]
    n = len(arr)

    import time
    t0 = time.time()
    print(product_array(arr))
    print(time.time()-t0)

    t0 = time.time()
    print(other_soln_one(arr, n))
    print(time.time() - t0)

    t0 = time.time()
    print(other_soln_two(arr, n))
    print(time.time()-t0)

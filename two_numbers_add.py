'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''


def two_numbers_addup(list_num, k):
    for n in list_num:
        temp = list_num.copy()
        remain = k - n
        temp.remove(n)
        if remain in temp:
            return True
    return False


if __name__ == "__main__":
    list_num1 = [10, 15, 3, 7]
    k1 = 17
    print(two_numbers_addup(list_num1, k1))
    print(two_numbers_addup(list_num1, 12))

    list_num2 = [3, 5, 12, 10, 10]
    k2 = 20
    print(two_numbers_addup(list_num2, k2))
    print(two_numbers_addup(list_num2, 24))

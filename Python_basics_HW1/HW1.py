import random as rn

def generate_random_list():
    """
    Generation of list with random numbers from 0 to 1000 inclusively
    :return: list of random numbers
    """
    return [rn.randint(0, 1000) for number in range(100)]

def swap(list, index1, index2):
    """
    swap values in a list of numbers
    :param list: list of numbers
    :param index1: the index for one value
    :param index2: the index for the second value
    """
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

def sort_list(list):
    """
    :param list: list of numbers, which assumed to be sorted
    :return: the sorted list
    """
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] < list[j]:
                swap(list, i, j)

    return list

def average(list, is_odd: bool):
    """

    :param list: from this parameter we take the values for calculating the average
    :param is_odd: define for what numbers we want to get average: for even numbers or odd ones.
    Should be True or False
    :return: average value for a set of even or odd numbers
    """
    # for defining what numbers we want to get: even or odd
    factor = 1 if is_odd else 0
    sum = 0
    count = 0
    for value in list:
        if value % 2 == factor:
            sum += value
            count += 1

    return sum / count

# generate list of random numbers
rn_numbers = generate_random_list()
#sort the list
sorted_rn = sort_list(rn_numbers)

# define average for even and odd numbers
even_average = average(sorted_rn, False)
odd_average = average(sorted_rn, True)

print(sorted_rn)
print(even_average)
print(odd_average)
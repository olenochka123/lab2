def selection_sort(array):
    """
        sorting our array
        :param array: our input array
        :return: our sorted array
        >>> selection_sort([0, 1, 2, 4, 3])
        [0, 1, 2, 3, 4]
        >>> selection_sort([8, 7, 19, 2, 9, 7])
        [2, 7, 7, 8, 9, 19]
        """
    for i in range(len(array)):
        minimum = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        array[minimum], array[i] = array[i], array[minimum]
    return array


def find_triplet_sum(array, sum):
    """
    search for triplet for the sum
    :param sum: our expected sum
    :param array: our input array
    :return: triplet for the sum
    >>> find_triplet_sum([3, 1, 0, 2, 4], 3)
    Yes: ( 0 , 1 , 2 )
    >>> find_triplet_sum([7, 2, 7, 8, 19, 9], 16)
    Yes: ( 2 , 7 , 7 )
    >>> find_triplet_sum([3, 1, 0, 2, 4], 20)
    No
    >>> find_triplet_sum([3, 1, 0, 2, 4], 20000000000000)
    Data input not correctly
    """
    length = len(array)
    if length >= 1000 or length < 3 or sum >= 3 * pow(10, 9) :
        return print('Data input not correctly')
    selection_sort(array)
    for i in range(0, length - 2):
        min_element = i + 1
        max_element = length - 1
        while min_element < max_element:
            if array[i] + array[min_element] + array[max_element] == sum:
                return print('Yes: (', array[i], ',', array[min_element], ',', array[max_element], ')')
            elif array[i] + array[min_element] + array[max_element] < sum:
                min_element += 1
            else :
                max_element -= 1
        return print('No')


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

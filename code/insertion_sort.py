def main():
    example = [5, 2, 4, 6, 1, 3]
    sorted = insertion_sort(example)
    print(sorted)


def insertion_sort(array):
    """This algorithm works by swapping larger elements
    to the left until they are in the right position,
    working from left to right on subsets of the array
    until every element has been sorted."""
    for (i, key) in enumerate(array):
        while i > 0 and array[i-1] > key:
            array[i] = array[i-1]
            i -= 1
        array[i] = key
    return array


main()

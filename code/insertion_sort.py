def main():
    example = [5, 2, 4, 6, 1, 3]
    sorted = insertion_sort(example)
    print(sorted)


def insertion_sort(array):
    for j in range(len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
    return array


main()

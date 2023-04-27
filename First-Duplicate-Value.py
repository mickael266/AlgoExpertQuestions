def firstDuplicateValue(array):

    for value in array:
        abs_value = abs(value)
        if array[abs_value-1] < 0:
            return value
        array[abs_value-1] *=-1

    return -1


def main():
    array = [2, 1, 10, 3, 4 , 5, 2, 7, 8, 9]
    print(firstDuplicateValue(array))


if __name__ == '__main__':
    main()
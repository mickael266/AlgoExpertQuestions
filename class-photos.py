def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()  # 1, 3, 4, 5, 8
    blueShirtHeights.sort() # 2, 4, 5, 6, 9
    
    size = len(redShirtHeights)
    front_row = ""

    if redShirtHeights[size-1] > blueShirtHeights[size-1]:
        front_row = "blue"
    elif redShirtHeights[size-1] < blueShirtHeights[size-1]:
        front_row = "red"
    else:
        return False

    for i in range(size):
        if front_row == "blue":
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
        else:
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
    return True
            


def main():
    #class_1
    redShirtHeights_1 = [5, 8, 1, 3, 4]
    blueShirtHeights_1 = [6, 9, 2, 4, 5]
    print(classPhotos(redShirtHeights_1, blueShirtHeights_1))


if __name__ == '__main__':
    main()
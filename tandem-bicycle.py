from audioop import reverse


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort() # [1,2,3,3,4,6]
    blueShirtSpeeds.sort() # [1,1,2,3,9,12]

    total_speed = 0 
    if fastest == True:
        for i in range(len(redShirtSpeeds)):
            if redShirtSpeeds[i] >= blueShirtSpeeds[i]:
                total_speed += redShirtSpeeds[i]
            else:
                total_speed += blueShirtSpeeds[i]

    else:  
        for i in range(len(redShirtSpeeds)):
            if redShirtSpeeds[i] <= blueShirtSpeeds[i]:
                total_speed += redShirtSpeeds[i]
            else:
                total_speed += blueShirtSpeeds[i]

    return total_speed



def main():
    red = [3, 3, 4, 6, 1, 2]
    blue = [1, 2, 1, 9, 12, 3]
   # print(tandemBicycle(red, blue, True)) #max speed
    print(tandemBicycle(red, blue, False))#min speed

if __name__ == "__main__":
    main()


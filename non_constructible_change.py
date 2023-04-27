def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    change = 0
    for coin in coins:
        if change+1 < coin:
            return change+1
        change += coin
    return change+1

    print(coins)

def main():
    coins_1 = [5, 7, 1, 1, 2, 3, 22] #excepted out output 20
    coins_2 = [1,2,5] #excepted out output 4
    coins_3 = [] #excepted out output 1

    print("coins_1", nonConstructibleChange(coins_1))
    print("coins_2" , nonConstructibleChange(coins_2))
    print("coins_3", nonConstructibleChange(coins_3))

if __name__ == "__main__":
    main()
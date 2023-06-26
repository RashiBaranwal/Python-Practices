# Function for Three way partitioning of an array around a given range
def threeWay(input1, lowVal, highVal):
# separate input list in three parts
    first = [ num for num in input if num<lowVal ]
    second = [ num for num in input if (num>=lowVal and num<=highVal) ]
    third = [ num for num in input if num>highVal]
# concatenate all three parts
    print(first + second + third)
# Driver program
if __name__ == "__main__":
    input1 = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
    lowVal = 14
    highVal = 20
    threeWay(input1, lowVal, highVal)
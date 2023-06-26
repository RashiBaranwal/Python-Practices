#This function finds factor of a number

def printFact(x):
    print("The factor of ",x,"are:")
    for i in range(1,x+1):
        if x%i == 0:
          print(i)
        
num = int(input("Enter a number to generate factors: "))
printFact(num)

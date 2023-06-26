marks = int(input("Enter your marks: "))

if marks>85 and marks<=100:
    print("Congo! You got A grade")
elif marks>60 and marks<=85:
    print("You got B grade")
elif marks>40 and marks<=60:
    print("You got B grade")
elif marks>30 and marks<=40:
    print("You got C grade")
else:
    print("You Failed the exam")
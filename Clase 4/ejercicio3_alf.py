num1 = float(input("please enter a number: "))
num2 = float(input("please enter another number: "))
if num2 == 0:
    print("error, you cannot divide by 0")
else:
    print(round(num1/num2,2))
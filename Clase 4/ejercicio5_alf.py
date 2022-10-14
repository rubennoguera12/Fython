age = int(input("please enter your age as an integer number: "))
salary = float(input("please enter your salary: "))
if age > 16 and salary >= 1000:
    print("you have to pay taxes")
elif age > 16 and salary < 1000:
    print("you should not be paying taxes")
else:
    print("you shouldn't even be worrying about taxes")

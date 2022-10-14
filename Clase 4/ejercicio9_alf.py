age = int(input("please enter your age as an integer number: "))
if 0 <= age < 4:
    print("you don't have to pay an entrance fee")
elif 4 <= age <= 18:
    print("you have to pay a 5$ entrance fee")
elif age > 18:
    print("you have to pay a 10$ entrance fee")
else:
    print("you cannot have a negative age, make sure you enter a correct age")
print('hello fython')
hours_worked = (input("Insert the number of hours you have worked: "))
price_per_hour = (input("Insert the rice per hour you have charged: "))
if type(hours_worked) is not int or type(price_per_hour) is not int:
    print("Invalid input, please enter an integer number ")
else:
    print(f"Vikua owes you {float(hours_worked)*float(price_per_hour)}")

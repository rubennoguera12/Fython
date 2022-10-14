edad = int(input("please enter your age as an integer number: "))
if edad >= 18 and edad < 100:
    print("you're over 18")
elif edad < 0:
    print("no way...")
elif edad >= 100:
    print("you might be death")
else:
    print("you're underage")

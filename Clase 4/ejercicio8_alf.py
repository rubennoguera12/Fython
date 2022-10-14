scorep = [0.0,0.4,0.6]
bonus =2400
score = float(input("please enter your score: "))
if score == scorep[0]:
    print("your performance was unacceptable, you'll receive 0$")
elif score == scorep[1]:
    print(f"your performance was acceptable, you'll receive a {scorep[1]*bonus}$ bonus")
elif score < 0.0:
    print(f"you may have entered a wrong score, try again")
elif score >= 0.6:
    print(f"you had an amazing performance you'll receive a {score*bonus}$ bonus")
else: 
    print(f"you may have entered a wrong score, try again")

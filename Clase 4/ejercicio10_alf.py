pizzatype = input("please enter the type of pizza you want, type V for vegetarian and R for regular: \n->  ")
if pizzatype.upper() == "V":
    vingredient = input("choose one option among the following ingredients: \n Bell-Pepper\n Tofu\ntype B for Bell-Pepper or T for Tofu\n ->")
    if vingredient.upper() == "B":
        print("your pizza will have tomato, mozzarella and bellpepper")
    elif vingredient.upper() == "T":
        print("your pizza will have tomato, mozzarella and tofu")
    else: 
        print("you may have entered an invalid ingredient, make sure you enter a valid ingredient next time")
elif pizzatype.upper() == "R":
    ringredient = input("choose one option among the following ingredients: \nPeperoni\nHam\nSalmon\ntype P for Peperoni, H for Ham or S for Salmon\n ->")
    if ringredient.upper() == "P":
        print("your pizza will have tomato, mozzarella and peperoni")
    elif ringredient.upper() == "H":
        print("your pizza will have tomato, mozzarella and ham")
    elif ringredient.upper()=="S":
         print("your pizza will have tomato, mozzarella and salmon")
    else:
        print("you may have entered an invalid ingredient, make sure you enter a valid ingredient next time")
else:
    print("you may have entered an invalid ingredient, make sure you enter a valid ingredient next time")
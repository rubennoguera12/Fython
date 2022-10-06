pizza = input("What kind of pizza are you looking for? Vegetarian or Traditional ")
if pizza == "Vegetarian":
    ingredient_v = input("Choose an ingredient: Bellpepper or Tofu")
    if ingredient_v == "Bellpepper":
        print("Your pizza toppings are: Mozzarella, tomato sauce and Bellpepper")
    elif ingredient_v == "Tofu":
        print("Your pizza toppings are: Mozzarella, tomato sauce and Tofu")
    else:
         print("Toppings not available")
elif pizza == "Traditional":
      ingredient_t = input("Choose an ingredient: Pepperoni, Jam, or Salmon")
if ingredient_t == "Pepperoni":
             print("Your pizza toppings are: Mozzarella, tomato sauce and Pepperoni")
elif ingredient_t == "Jam":
            print("Your pizza toppings are: Mozzarella, tomato sauce and Jam")
elif ingredient_t == "Salmon":
             print("Your pizza toppings are: Mozzarella, tomato sauce and Salmon")
else:
         print("Toppings not available")
else:
    print("Pizza not available")

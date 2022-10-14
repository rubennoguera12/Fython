password = "clave12345"
while True:
        answer = input("please enter your password: ")
        answer = answer.upper()
        if answer == password.upper(): 
                print("that's correct, you're now logged into the program")
                break
        else: 
            print("that's not correct") 
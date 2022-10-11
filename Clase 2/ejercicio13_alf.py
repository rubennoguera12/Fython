getout = "Getout"
while True:
        answer = input("please write anything you'd like to print on the screen, if you don't want to print anything write getout: ")
        if answer.title() == getout: 
                print("Ok we'll let you leave")
                break
        else: 
            print(answer)
electronicmail = input("please type your email: ")
mailnew = electronicmail.split("@")
print(electronicmail.replace(mailnew[1],"ceu.es"))
print(mailnew)
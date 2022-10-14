taxrate = [0.05,0.15,0.2,0.3,0.45]
print(taxrate)
rent = float(input("please enter your anual rent: "))
if rent <= 10000:
    print(f"your anual tax rate is {taxrate[0]*100}%")
elif rent > 10000 and rent <= 20000:
    print(f"your anual tax rate is {taxrate[1]*100}%")
elif rent > 20000 and rent <= 35000:
    print(f"your anual tax rate is {taxrate[2]*100}%")
elif rent > 35000 and rent <= 60000:
    print(f"your anual tax rate is {taxrate[3]*100}%")
else:
    print(f"your anual tax rate is {taxrate[4]*100}%")
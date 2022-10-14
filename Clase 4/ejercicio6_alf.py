sex = input("please enter your sex, type M if you are a male, or F if you are a female: ")
name = input("please enter your name: ")
name = name.lower()
lista1 = "a,b,c,d,e,f,g,h,i,j,k,l,m"
lista1 = lista1.split(",")
lista2 = "n,nh,o,p,q,r,s,t,u,v,w,x,y,z"
lista2 = lista2.split(",")
if name[0] in lista1 and sex == "F":
    print("you belong to group A")
elif name[0] in lista2 and sex == "M":
    print("you belong to group A")
else:
    print("you belong to group B")


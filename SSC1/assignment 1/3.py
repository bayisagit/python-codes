name=input("enter your name ")
height=int(input("enter your height "))
weight=int(input("enter your weight "))
choose=input("if you want to know your body mass index enter yes/no ")
if choose=="yes":
    bmi=weight/(height*height)
    print("name    height     weight    bmi")
    print(name,   height,    weight,    bmi)
else:
    print("name    height     weight    bmi")
    print(name    ,height     ,weight)
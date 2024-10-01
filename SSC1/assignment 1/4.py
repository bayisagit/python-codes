value = int(input("enter the number "))
choise = input("would you want the squared or cubed")
if choise=="squared":
    print(value*value*value)
elif choise=="cubed":
    print(value*value)
else:
    print("your choise not perfect make it perfect and try again")
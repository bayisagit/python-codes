'''
numbers=[3,6,2,8,4,10]
number2=numbers.copy()
numbers.append(10)


print(number2)

numbers=[2,2,3,4,4,4,3,6,7,8]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

costumer= {
    "name":"johb smith",
    "age": 30,
    "is_verified": True
    
}
 
print(costumer.get("name"))

message=input(">")
words=message.split(' ')
print(words)

def greet_user():
    print('hi there')
    print('welcome aboard')


print('start')
greet_user()
print('end')
 '''
def square(number):
    print( number*number)
print(square(4))



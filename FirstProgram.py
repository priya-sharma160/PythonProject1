'''
from multiprocessing.managers import SharedMemoryManager
#print('It\'s nice to meet you')
#print("My name is Priya Sharma\U0001F605")
#emoji(Control+Command+space)
#print("Hello!\nHow are you?")#nextline
#print("Hello!\tHow are you?")#tab

(name = "Priya"
surname = "Sharma"
fullname = name + " " + surname
print(fullname))
name = "My name is Priya"
surname = "My surname is Sharma"

print(name,'=' * 83, surname)
cats = input("How many cats do you have?")
print(cats)
catsint = int(cats)
doublecats = 2*catsint
print(doublecats)
print("I have " + str(doublecats) + " cats ")
#print(f"I have {a} apples")
print(math.pi)
print(math.sqrt(23))
import math

pinumber = math.pi
print(f"number pi with 2 decimal is {pinumber:.2f}")
fahrenheit_str = input("Enter a temperature in Fahrenheit")
print(type(fahrenheit_str))
celsius = (fahrenheit-32)*5/9)

num = int(input("Enter a number: "))
if 0 < num <1000:
    print("Positive")
#if num < 0:
    #print("Negative")
if num == 0:
    print("Zero")
if num >= 1000:
    print("very large integer")
if num <= -1000:
    print("very small integer")
if -1000 < num < 0:
    print("negative")
result ="win"
if result == "win":
    print("You won your bet")
elif result == "lose":
    print("You lose your bet")
else:
    print("That was a draw")
num = int(input("Enter a number: "))

if num >= 1000:
    print("very large integer")
elif 0 < num < 1000:
    print("Positive")
elif num == 0:
    print("Zero")
elif -1000 < num < 0:
    print("negative")
else:
    print("very small integer")
time = float(input("Enter current time: "))

if 5 <= time <= 11:
    print("Good Morning")
elif 12 <= time <= 17:
    print("Good Afternoon")
elif 18 <= time <= 21:
    print("Good Evening")
elif 21 <= time <= 23:
    print("Good Night")
else:
    print("Invalid")
age = int(input("Enter your age: "))
if age>=65:
    print("You are retired.")
elif age>=18:
    print("You are working-age.")
elif age>=7:
    print("You are in school.")
else:
    print("You are a small child.")
age = int(input("Ask for the person age: "))
if age < 5:
    print("Free.")
elif 5 <= age <=17:
    print("7$.")
elif 18 <= age <=59:
    print("12$")
else:
    print("8$")
# from 1 to 10 counting
count = 1

while count <= 10:
    print(count)
    count = count + 1
a = 10
b = 5
print(a % b) # Modulo
count = int(input("please enter your countdown number:"))
#count = 3
print("Countdown starting ...")

while count >= 0:
    print(count)
    count = count - 1
print ("Kaboom!")

num = int(input("please enter your countdown number:"))
#count = 3
print("Countdown starting ...")
while num >= 0:
    if num % 2 == 0:
        print(num)
    num -= 1

correct_password = "james"
user = input("Please enter password")

while user != correct_password:
    user = input("Please enter password")
    print("Access")

secretnum = 3

while secretnum != 7:
    secretnum = int(input("Enter number: "))
print("Execution stopped.")

die = random.randint(1,6)

print(f'You rolled {die}')


die = 0


while die != 6: # while true we dont get out from loop getout from loop break
    die = random.randint(1, 6)
    if die != 6:
        print("Try again")

print("You got a 6!")

die = 0
while True:
    die = random.randint(1, 6)
    print(die)
    if die != 6:
        print("Try again")
    if die == 6:
        break

print("You got a 6!")

roll = 0

while die != 6:
    die = random.randint(1, 6)
    roll = roll + 1
    if die != 6:
        print("Try again")

print(f"You got a 6 in {roll} rolls!")

first = 1
while first <= 3:
    second = 1
    while second <= 3:
        print(f"{first} times {second} is {first*second}")
        second = second + 1
        first = first + 1


command = input("Enter command")
while command!="stop":
    if command=="Mayday":
        break
    print("Executing command: " + command)
    command = input("Enter command:")
print("Execution stopped.")

names = ['Alice', 'Bob', 'Carmen', 'David', 'Eve', 'Fred', 'George', 'Harry']
#print(names[-3: -7: -1])
#start: stop: step
# print(names[::-1])
for item in names:
    print(item)

for number in range(100, -1, -3):
    print(number)

    names = ['Alice', 'Carmen', 'David', 'Eve', 'Alice', 'George', 'Harry']
#names.append('John')
# names.remove('Alice')
# names.insert(2,'Honey')
# ind = names.index('Alice')
names.sort(reverse=True)
print(names)

numbers = [4, 1, -5, 9, -1, 12, -3]
#names.append('John')
# names.remove('Alice')
# names.insert(2,'Honey')
# ind = names.index('Alice')
# numbers.sort(reverse=True)
# numbers.sort()
print(numbers)
'''
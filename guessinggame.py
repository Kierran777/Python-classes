import random
numbers=["0","1"]

selection=input("what number do you want, 1. 0, 2. 1 any other quit")
selectedIndex=random.randint(0,1)
computerChoice=numbers[selectedIndex]

if selection==computerChoice:
    print("You have won")
else:
    print("You have lost")

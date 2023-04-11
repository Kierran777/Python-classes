import random
choices=["rock","paper","scissors"]
isgamecontinuing=True
#declare variable computerscore and userscore and set them to 0
compscore=0
userscore=0
while isgamecontinuing:
    selection=input("what choice do you want, 1.rock, 2.paper, 3.scissors any other choice quit")
    selectedChoice=selection.lower()

    if selectedChoice not in choices:
        exit()

    selectedIndex=random.randint(0,2)
    computerChoice=choices[selectedIndex]

    print("computer choice was"+ computerChoice)
    print("your choice was"+ selectedChoice)

    if selectedChoice=="rock" and computerChoice=="rock":
        print("draw")
    elif selectedChoice=="rock" and computerChoice=="paper":
        print("You have lost")
        compscore=compscore+1
        #computerscore should be updated that is compscore=compscore+1
    elif selectedChoice=="rock" and computerChoice=="scissors":
        print("You have won")
        userscore=userscore+1
        #userscore=userscore+1
    elif selectedChoice=="paper" and computerChoice=="paper":
        print("draw")
    elif selectedChoice=="paper" and computerChoice=="rock":
        print("You have won")
        userscore=userscore+ 1
    elif selectedChoice=="paper" and computerChoice=="scissors":
        print("You have lost")
        compscore = compscore + 1
    elif selectedChoice=="scissors" and computerChoice=="scissors":
        print("draw")
    elif selectedChoice=="scissors" and computerChoice=="rock":
        print("You have lost")
        compscore = compscore + 1
    elif selectedChoice=="scissors" and computerChoice=="paper":
        print("You have won")
        userscore = userscore + 1
    #if userscore or compscore has reached 5 print whoever has won
    if userscore==5:
        print("User has won")
        exit()
    elif compscore==5:
        print("Computer has won")
        exit()

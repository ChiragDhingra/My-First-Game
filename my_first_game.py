import random
from re import T

def GameWin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you =='g':
            return True
    elif comp  =='w':
        if you =='g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return True
        elif you == 'w':
            return False
    
    




print("Computer turn: Snake(s) Water(w) Gun(g) ?")
randNo =random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo ==2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your turn: Snake(s) Water(w) Gun(g) ?")
a = GameWin( comp ,you)

print(f"Computer chose:{comp}")
print(f"You chose:{you}")

if you == comp:
    print("The match ties")
elif a:
    print("You lose the match")

else:
    print("You win the match")


        
import random
rock='''  _ __    ___     ___  | | __
 | '__|  / _ \   / __| | |/ /
 | |    | (_) | | (__  |   < 
 |_|     \___/   \___| |_|\_\ 
 '''
paper='''  _ __     __ _   _ __     ___   _ __ 
 | '_ \   / _` | | '_ \   / _ \ | '__|
 | |_) | | (_| | | |_) | |  __/ | |   
 | .__/   \__,_| | .__/   \___| |_|   
 |_|             |_| 
 '''
scissor='''               _                            
  ___    ___  (_)  ___   ___    ___    _ __ 
 / __|  / __| | | / __| / __|  / _ \  | '__|
 \__ \ | (__  | | \__ \ \__ \ | (_) | | |   
 |___/  \___| |_| |___/ |___/  \___/  |_|
 '''

choose=int(input("Enter 1 for rock, 2 for paper & 3 for scissor\n"))
computer=random.randint(1,3)
print(computer)
if computer==1 and choose==3:
    print("You win")
elif computer==1 and choose==2:
    print("You lose")   
elif computer==2 and choose==3:
    print("You win")
elif computer==2 and choose==1:
    print("You lose")
elif computer==3 and choose==1:   
    print("You win")
elif computer==3 and choose==2:   
    print("You lose")
elif computer==choose:   
    print("Tie")   

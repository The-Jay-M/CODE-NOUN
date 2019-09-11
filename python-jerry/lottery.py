from random import randint
doNotPick= []
while (len(doNotPick) < 6):
    generate= randint(1, 37)
    if (generate in doNotPick):
        pass
    else:
         doNotPick.append(generate)
#To print out values from the doNotPickList we need an index.
#Indexing starts from 0.
print(doNotPick[0])
print(doNotPick[1])
print(doNotPick[2])
print(doNotPick[3])
print(doNotPick[4])
print(doNotPick[5])

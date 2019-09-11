from random import randint
card_number= ""
while ((len(card_number) < 17)):
    generate= randint(0,9)
    card_number= card_number + str (generate)
print (card_number)

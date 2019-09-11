import re

#find all was the bloody thing!
print("Welcome to Vowel Finder!!!")
findx = input("Type in a sentence: ")
findr = findx.split()


pattern = r"[aeiou]"

same = re.findall(pattern, findx)

patterno = r"Kiitan"

samex = re.search(patterno, findx)

changer = re.sub(patterno, "JERRY", findx)

def new_input():
    print("\n\nnow that we have established your propensity\nfor directness...")
    print("\nlet me extract your email address from a string\nVIA MAGIC!!! hehe")
    findq = input("type in a string containing a simple email address: ")
    pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
    sameq = re.search(pattern, findq)
    if sameq:
        print("That's a valid response!")
        print("YOUR EMAIL ADDRESS: {}".format(sameq.group()))
    else:
        print("That's an invalid response")
        pass
if same:
    print("There are {} vowels in your sentence".format(len(same)))
    new_input()
    if samex:
        print(changer)
    else:
        pass
else:
    print("There are no vowels in your sentence")


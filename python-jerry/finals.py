for i in range(10):
    try:
        if 10/i == 2.0:
            break
    except ZeroDivisionError:
        print(1)
    else:
            print(2)
for i in range(5):
	print(i)

lang = input("input: ")
name = input("name: ").upper()
count = input("count: ").split()
for i in count:
    print(i)
    
count_max = max(count)


def greet(lang):
    if lang == "en":
        return "Hello"
    elif lang == "fr":
        return"Bonjour"
    elif lang == "es":
        return "Hola"
    else:
        return "Greeting Unknown"
print(greet(lang), name)
print("Max letter is", count_max)


greet(lang)

#def trisha():
    #return "Hello"
#print(trisha(), "Edwina")

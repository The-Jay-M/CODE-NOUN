text = input(str("do stuff: "))

texty = text.split()
print(texty[0].upper())


texty_a = text.strip()
print(texty_a)

print(text)

if "y" in text:
    print(text.replace("y", "X"))


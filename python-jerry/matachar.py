import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "grry"):
    print("Match 3")

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
    print("Match 1")
    
if re.search(pattern, "qwertyuiop"):
    print("Match 2")

if re.search(pattern, "arhythme imythso u"):
    print("Match 3")

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
    print("Match 1")

if re.search(pattern, "E3"):
    print("Match 2")

if re.search(pattern, "lab"):
    print("Match 3")

pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
    print("Match 1")

if re.search(pattern, "AbCdEfG123"):
    print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")

pattern = r"egg(spam)*"

if re.match(pattern, "egggspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")

pattern = r"ice(-)?cream"

icecream = re.match(pattern, "icecream")

if re.match(pattern, "icecream"):
    print("Match 1")

if re.match(pattern, "ice-cream"):
    print("Match 2")

if re.match(pattern, "sausages"):
    print("Match 3")

if re.match(pattern, "ice-ice"):
    print("Match 4")

pattern = r"9{1,3}$"

if re.match(pattern, "9"):
    print("Match 1")

if re.match(pattern, "999"):
    print("Match 2")

if re.match(pattern, "9999"):
    print("Match 3")

    





















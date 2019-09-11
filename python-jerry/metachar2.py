import re

pattern = r"egg(spam)"

if re.match(pattern, "eggspam"):
    print("hey")

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")

if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")

if match:
    print(match.group("first"))
    print(match.groups())

pattern = r"(a)(b(?:c)(d)(?:e))"

match = re.match(pattern, "abcdefghijkl")

if match:
    print(len(match.groups()))

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")

if match:
    print("Match!")
else:
    print("No match")

import re
def pinky():
    str = r" I am \r\a\w!"
    print(str)

pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")

#if re.match(pattern, "blue"):
    #print("Match 2")

if re.match(pattern, "gray"):
    print("Match 3")
    
#pinky()

def metachar():
    stringly = ["spam", "spum", "spim","sram"]
    string_pattern = "sp.m"
    for str in stringly:
        if re.match(string_pattern, str):
            print("{} matches \t\t\t{}".format(str, string_pattern))
        else:
            print("{} doesn't match \t\t{}".format(str, string_pattern))

metachar()
    

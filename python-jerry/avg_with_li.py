x= list()
while True:
    b=input("yeah? ")
    if b == "no" : break
    y = float(b)
    x.append(y)
   
p = sum(x) / len(x)
print("Avg: ", p)

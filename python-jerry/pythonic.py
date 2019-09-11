numbers = ("a", "b", "c")
x, y, z = numbers
print(x)
print(y)
print(z)
x, z = y, x
print(x,z)

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)

for i in range(10):
    if i > 5:
        print(i)
        break
else:
    print(7)

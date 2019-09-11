def function(x, y, food="spam"):
    print(food)

function(1, 2)
function(3, 4, "egg")

def my_func(x, y=7, *lala, **lalavalue):
    print(lalavalue)

my_func(2, 3, 4, 5, 6, a=7, b=8)

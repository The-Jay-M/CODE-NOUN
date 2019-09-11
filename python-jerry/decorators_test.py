def decor(func):
    def wrap():
        print("===============")
        func()
        print("===============")
    return wrap

def print_text():
    print(" Hello World!")

print_text = decor(print_text)
print_text();


def decor1(func):
    def wrap1():
        print("**************")
        func()
        print("**************")
    return wrap1

@decor
@decor1
def print_text():
    print(" Hello World!")

print_text();

    

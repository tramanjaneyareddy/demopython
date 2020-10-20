def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            return "Whoops! cannot divide"

        else:
            return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    return a / b

a=divide(2, 5)
print(a)
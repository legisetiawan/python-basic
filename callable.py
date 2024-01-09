# type operasi pemanggilan fungsi mengembalikan nilai boolean
print("callable booleans :")
print(type(callable(str)))
print("check callable :")
def Callable():
    return "tests"
x = Callable
y = callable
print(type(x))
print(type(y))
print(callable(y))
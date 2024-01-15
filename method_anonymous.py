# currying / anonymous
import os
def pangkat(n):
    return lambda x:x**n
a = pangkat(2)
b = pangkat(3)
os.system("cls")
print(f"Pangkat 2 = {a(5)} ")
print(f"Pangkat 3 = {b(5)} ")
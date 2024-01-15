# Menetukan type suatu argument method
import os
def jumlah(one:int,two:int):
    tambah = one + two
    print(f"Hasil Tambah {one} dan {two} = {tambah} ")
    return tambah
def kuadrat(bil1:int):
    kuadrat = bil1**2
    print(f"Hasil Kuadrat {bil1} = {kuadrat}")
    return kuadrat
def kubik(bil1:int):
    kubik = bil1**3
    print(f"Hasil Kubik {bil1} = {kubik} ")
    return kubik
def no_hints(argument:int): # mengembalikan type data  yg di tentukan
    nohints = 10**argument
    print(f"Hasil nohints Sepuluh pangkat  {argument} = {nohints} ")
    return nohints
def hints(argument:int)->int: # mengembalikan type data  yg di tentukan
    hints = 10**argument
    print(f"Hasil hints Sepuluh pangkat  {argument} = {hints} ")
    return hints
os.system("cls")
# print("MATEMATIKA")
# print("*"*80)
# jumlah(2,3.3)
# kuadrat(2.4)
# kubik(2)
nohints = no_hints(2.2)
print(nohints) 
hints = hints(2.2) # Note......................................???
print(hints)
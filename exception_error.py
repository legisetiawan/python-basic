# program error saat runtime gunakan try
from numbers import Number # check apakah input angka 
import os

os.system("cls")
def tambah(a,b):
    if not isinstance(a, Number) or not isinstance(b,Number): # not number or not number True
        raise "input pertama harus angka"
    return a+b

def bagi():
    while (True):
        angka = int(input("Angka: "))
        try:
            hasil = 10/angka
            print(f"Hasil {hasil}")
            is_done = input("lanjutkan..!! (y/n)")
            if is_done == "n":
                break
        except: # jika program runtime (saat di run) error
            if angka == 0:
                print("Input Tidak boleh 0 ...!!!")  



print(tambah(5,4))
bagi()

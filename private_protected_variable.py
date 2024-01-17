import os
class Person:
    def __init__(self,nama:str,umur:int):
        self.nama = nama
        self.umur = umur
        self.__tgl_lahir = "tgl_lahir" # private variable 2 garis bawah
        self._alamat = "alamat" # private variable  garis bawah, value bisa di ubah
os.system("cls")
P1 = Person("andi",23)
print(P1.nama)
print(P1.umur)
# print(P1.__tgl_lahir)
P1._alamat = "jl.soekarno"
print(P1._alamat)

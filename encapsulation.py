# pastikan variable private Untuk mengambil gunakan set dan get 
import os

class Person:

    def __init__(self,nama,umur,tgl_lahir):
        self.__nama = nama # variable private
        self.__umur = umur # variable private
        self.__tgl_lahir = tgl_lahir # variable private

    # get
    def getName(self):
        return self.__nama
    # get
    def get_tgl_lahir(self):
        return self.__tgl_lahir
    # set
    def set_tgl_lahir(self,set_tgl_lahir):
        self.__tgl_lahir =  set_tgl_lahir

os.system("cls")
one = Person("andi",18,19112000)
print(one.__dict__)
print(f" Get : {one.getName()}")
print(f" Set : {one.get_tgl_lahir()}") # ambil tgl lahir dan ubah
print(f" Set : {one.set_tgl_lahir_lahir("19101999")}")
print(one.__dict__)
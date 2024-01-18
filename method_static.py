import os
# Statict method (decorator) mengambil privat variable dengan anotasi @staticmethod bisa di gunakan untuk Class dan Object isntance dari class.
class Person:
    """docstring for Person."""
    # variable class
    __jumlah_person = 0

    def __init__(self, nama,umur,tgl_lahir):
        self.nama = nama
        self.umur = umur
        self.tgl_lahir = tgl_lahir
        Person.__jumlah_person += 1

    def get_jumlah_person(self ): # self berlaku untuk object
        return Person.__jumlah_person 
    
    def get_jumlah_person(): # Tidak berlaku untuk object
        return Person.__jumlah_person 
    
    @staticmethod
    def get_jumlah_static(): #  berlaku untuk object dan class.......!?
        return Person.__jumlah_person 


os.system("cls")
P1 = Person("anto",45,"01081788")
print(f"Peson Pertama Menggunakan static Method : {P1.get_jumlah_static()}") 

P2 = Person("diana",25,"11031988")
print(f"Person kedua : Menggunakan static Method : {P2.get_jumlah_static()}")

print(f"GET JUMLAH  MENGGUNAKAN STATIC UNTUK JUMLAH DALAM CLASS : {Person.get_jumlah_static()}") 

print(f"Nama :{P1.nama}")
print(f"Umur :{P1.umur}")
print(f"Tgl lahir :{P1.tgl_lahir}")



    
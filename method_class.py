import os
# Class method (decorator) mengambil privat variable dengan anotasi @classmethod bisa di gunakan untuk Class dan Object isntance dari class (Polymorphism).
class Person:
    """docstring for Person."""
    # variable class
    __jumlah_person = 0

    def __init__(self, nama,umur,tgl_lahir):
        self.nama = nama
        self.umur = umur
        self.tgl_lahir = tgl_lahir
        Person.__jumlah_person += 1
    
    @classmethod
    def get_jumlah_class(cls): # ada argument static method tidak ada argument
        return cls.__jumlah_person 


os.system("cls")
P1 = Person("anto",45,"01081788")
print(f"Person Pertama Menggunakan class Method dari class : {Person.get_jumlah_class()}") 
print(f"Person Pertama Menggunakan class Method dari object : {P1.get_jumlah_class()}") # Polymorphism




print(f"Nama :{P1.nama}")
print(f"Umur :{P1.umur}")
print(f"Tgl lahir :{P1.tgl_lahir}")



    
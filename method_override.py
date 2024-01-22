import os

class Siswa:
    def  __init__(self, name, age):
        self.name = name
        self.age = age
        
    def  info(self):
        print("{} saat ini umur sudah: {}".format(self.name,self.age))
        
class Siswi(Siswa):
    def  __init__(self, name):
        super().__init__(name,34)
        
    def  info(self):
        print("{} saat ini, \n\tumur sudah: {}".format(self.name,self.age)) # override method menimpa method denga nama yg sma block code yg berbeda.
os.system("cls")   
nana = Siswi("nana")
nana.info()
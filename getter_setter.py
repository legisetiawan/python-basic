import os
class Person:
    """docstring for Person."""
    def __init__(self, name,umur,berat):
        self.name = name
        self.__umur = umur
        self.__berat = berat
        #self.__info = "name {} : \n\t umur: {}".format(self.name, self.__umur)
        
    @property
    def info(self):
        return "name {} : \n\t umur: {}".format(self.name, self.__umur)
    
    @property
    def berat(self):
        pass      

    @berat.getter  # ambil variable berat
    def berat(self):
        return self.__berat
    
    @berat.setter  # ubah variable berat
    def berat(self,nb):
       self.__berat = nb

    @berat.deleter  # ubah variable berat
    def berat(self):
       print("Berat di hapus.")
       self.__berat = None
    
os.system("cls")
p1 = Person("dika",34,40)

print(p1.info)  
p1.name = "ucok"
print(p1.info)
print(p1.__dict__)

print("Settet getter berat :")
print(f" Get berat :{p1.berat}") # get berat
p1.berat = 35 # ubah data berat
print(f" Set berat :{p1.berat}") # set berat
print(p1.__dict__)
del p1.berat
print(p1.__dict__)

    
import os
# magic method ditandai dengan __method__
class Jeruk:
    def __init__(self,nama,jumlah) :
        self.nama  = nama
        self.jumlah  = jumlah
    def __repr__(self) :
        return "Debug - jeruk:{} jumlah:{}".format(self.nama,self.jumlah)
    
    def __str__(self) :
        return "jeruk:{} jumlah:{}".format(self.nama,self.jumlah)
    
    def __add__(self,objek) :
        return self.jumlah + objek.jumlah
    @property # harus di tambah dengan decorator property
    def __dict__(self) :
        return "Nama dan jumlah"
os.system("cls")
belanja1 = Jeruk("sunkis",23)
belanja2 = Jeruk("nipis",13)
print(belanja1)
print(belanja2)
print(f"Total Jumlah jeruk :{belanja1 + belanja2}")
print(belanja1.__dict__)
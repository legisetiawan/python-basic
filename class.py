
class Murid():

    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
class Siswa(Murid):
    def __init__(self,nama,):
        Murid.__init__(self,nama,9)
class Siswi(Murid):
    def __init__(self,nama):
        Murid.__init__(self,nama,8)
        
      
     
S1 = Siswa("Anto")
S2 = Siswi("Ana")
print(f"Nama Siswa :  {S1.nama} Umur : {S1.umur}")
print(f"Nama Siswi :  {S2.nama} Umur : {S2.umur}")

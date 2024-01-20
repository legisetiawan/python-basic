# mewarisi / inheritance method parent
import os

class Siswa:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    def info(self):
        print("{} saat ini umur: {}".format(self.nama, self.umur))
        
class Siswi(Siswa):
    def __init__(self, nama):
        super().__init__(nama,45)
        super().info()
os.system("cls") 
dian = Siswi("dian")
class Siswa():
    """docstring for Siswa."""
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
        
kelas_satu = Siswa("andi",7,21) 
kelas_dua = Siswa("ana",8,24) 
print(kelas_satu.__dict__)
print(kelas_dua.__dict__)
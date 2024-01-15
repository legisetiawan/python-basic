# variable tempat menyimpan data(all data), global bisa di gunakan oleh class dan method, local hanya di class atau method saja bisa di gunakan
import os
nama = "ani" # variable global
gumur = 15
def get_nama():
    print(f"Mencari index dan nilai")
    return nama
def get_umur(angka):
    global gumur # menngakses global variable di dalam methods
    gumur = angka
os.system("cls")
get_nama()

# for i in range(5):
#     print(f" Indek ke {i} {nama.upper()} adalah variable global")


five = 5
for i in range(0,5): # FOR DAN IF bisa menggunakan variable global jika manipulasi pastikan data tidak berpengaruh ke data utama.....???
    five += i
    print(f" nilai di tambah dengan range 0,1,2,3,4  {i} :{five}")
# print(f"angka global sebelum {gumur}")
# get_umur(14) 
# print(f"angka global setelah {gumur}")
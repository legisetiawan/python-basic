from copy import deepcopy
a = [1,2]
b = [3,4]
c = [a,b]
d = c.copy() # data yg di copy di dalam list jika angka dapat di ubah file utama tetap, jika list data di ubah file utama dan copianya berubah juga. makanya gunakan deepcopy jangan lupa import duluya.

# MANIPULASI
c[1][0] = 6 # data asli dan copy sama2 berubah karna alamat index ke 0 dan seterusnya SAMA.
# PRINT
# print("PRINT :")
# print(f"Data Asli {c}")
# print(f"Ambil data Asli by index 0 : {hex(id(c[0]))} alamat index ke 0 SAMA.")
# print(f"Address Asli {hex(id(c))} Alamat berbeda,")
# print(f"Data Copy {d}")
# print(f"Ambil data Copy by index 0 : {hex(id(d[0]))} alamat index ke 0 SAMA.")
# print(f"Address Copy {hex(id(d))} Alamat berbeda,")
# DEEP COPY
print("DEEP COPY :")
e = [a,b,10]
deep = deepcopy(e)
deep[1][0]= 8 # data asli tidak berubah berbeda.....?
# Print
print(f"Data Asli {e}")
print(f"Data Asli {hex(id(e))} kan beda address memori.!! ")
print(f"Data Deep {deep}")
print(f"Data Deep {hex(id(deep[0]))} kan beda address memori.!!")

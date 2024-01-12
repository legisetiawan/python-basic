# kumpulan index terbatas yg di index oleh kumpulan index arbitrer, jenis ada satu yaitu DICT data terdiri dari key dan value 
tamba_warna = input("Warna:")
warna = input("warna apa:")
dict = {
        "brand" : "honda",
        "model" : "Hornet CB",
        "year" : 1987
        }
dict["lokasi"] = "jowo"
dict["harga"] = 300000
dict[tamba_warna] = warna # menambah data dari input
del dict['harga']
# print(dict["brand"])
# print(dict["year"])
# print(dict["warna"])
print(dict)




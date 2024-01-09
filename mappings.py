    # kumpulan index terbatas yg di index oleh kumpulan index arbitrer, jenis ada satu yaitu DICT data terdiri dari key dan value 
dict = {
        "brand" : "honda",
        "model" : "Hornet CB",
        "year" : 1987
        }
dict["lokasi"] = "jowo"
dict["harga"] = 300000
del dict['harga']
print(dict["brand"])
print(dict["year"])
print(dict["lokasi"])
print("type data:", type(dict))




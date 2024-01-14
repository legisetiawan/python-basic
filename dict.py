# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary JIKA MENGUNAKAN copy() di file utama data tidak berubah....!
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary
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




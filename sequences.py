#type data urutan list, tuple, range.
list = ["a","b","c"]
print(list)
print('bil pertama:')
print(list[0]) #mengambil bilangan pertama
print('bil kedua:')
print(list[2]) #mengambil bilangan keduas

#Type data tuple type data yg tidak bisa di ubah, string, byte
tuple =("ani","budi")
print(tuple)
print(tuple[0])
# perbedaan list dengan tuple data tuple tidak bisa di ubah
list = ["a","b"] 
list.insert(2,"c") # menyisipkan data dengan method insert(index,data)
list.insert(2,"d")   
tuple = ("a","b")
list[0] = "b"
print(list)
print(tuple)
print('list tuple')
# type data range
range = range(11)
print(range)
print(range[1])
#Type data yg  bisa di ubah list , array byte
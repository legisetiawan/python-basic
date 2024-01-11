# jika ingin mengambil data dari sebuah method bisa di simpan di variables
def jumlah_list(*list_float):
    total = 0.0
    for angka in list_float:
        total = total + angka
    return (list_float,total)
list_float,total = jumlah_list(23.0,23.9,12.9,4.3)
print(total)
print(f"Total penjumlahan :{list_float} = {total}") # karna gak bisa mengakses list_float, retun di buat tuple
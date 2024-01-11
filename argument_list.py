# jika kita memiliki argument lebih dari satu, bisa menggunakan list argument sebelum argument *argument= value disimpan paling terakhir jika ada argument lain buat di awal argument
def jumlah_list(*list_float):
    total = 0.0
    for angka in list_float:
        total = total + angka
    print(f"Total penjumlahan : {list_float} = {total}")
jumlah_list(23.0,23.9,12.9,4.3)
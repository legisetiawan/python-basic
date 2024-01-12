# jika kita memiliki argument lebih dari satu, bisa menggunakan list argument sebelum argument *argument= value disimpan paling terakhir jika ada argument lain buat di awal argument
def penjumlahan(*list_float):
    total = 0.0
    for angka in list_float:
        total += angka
    print(f"Total penjumlahan : {list_float} = {total}")

def pengurangan(*list_float):
    kurang = list_float
    for angka in list_float:
        kurang = kurang - angka
    print(f"Total pengurangan {list_float} = {kurang} ")


def perkalian(*list_float):
    kali = 0.0
    for angka in list_float:
        kali * angka
    return kali

def pembagian(*list_float):
    bagi = 0.0
    for angka in list_float:
        bagi /= angka
    return bagi
pengurangan(23,3,2,4)
kali = perkalian(3,3,2,4)
bagi = pembagian(23,3,2,3)
penjumlahan(23.0,23.9,12.9,4.3)
print("kurang :")
# print(kurang)
print("kali :")
print(kali)
print("Bagi :")
print(bagi)
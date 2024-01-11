# memberhentikan eksekusi code jika kondisi tertentu
for i in range(1,51):
    if i % 8 == 0:
        break
    print(i)

while True:
    data_ganjil = int(input("Masukan bilangan genap :"))
    if data_ganjil % 2 == 0:
        break
    print(data_ganjil)
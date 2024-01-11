# fitur input data python default value string harus di convert jika ada operator matematika
def data_diri():
    print('Isi data form input :')
    nama = input("masukan Nama :")
    tahun_lahir = int(input("masukan tahun_lahir :"))
    umur = 2024 - tahun_lahir
    if umur <= 15:
        print(f"Masih Bocill")
        print(f'Umur Anda {umur} tahun ')
        print(f"rajin belajar Bocill")
    elif umur==22 and umur<=27:
         print(f"lumayan tua {nama} cepat cari istri")
    else:
        print(f'Umur Anda {umur} tahun sudah koloot')
        print(f'Okeee....!! {nama} harusnya udah punya anak.... Lobaa')

data_diri()

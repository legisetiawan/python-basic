import datetime
S241 ={
    "nis":"241",
    "nama":'andi',
    "kelas":"III",
    "tempat_lahir":"jakarta",
    "tgl_lahir":datetime.datetime(2014,4,10),
    "beasiswa":False
}
S242 ={
    "nis":"242",
    "nama":'anto',
    "kelas":"V",
    "tempat_lahir":"jambi",
    "tgl_lahir":datetime.datetime(2012,4,2),
    "beasiswa":False
}
S243 ={
    "nis":"243",
    "nama":'naila',
    "kelas":"IV",
    "tempat_lahir":"riau",
    "tgl_lahir":datetime.datetime(2016,1,21),
    "beasiswa":True
}
siswa = {
    "S241":S241,
    "S242":S242,
    "S243":S243,
}
print(f"{'NIS':<16} {'NAMA':<16} {'Kelas':<15} {'Tempat lahir':<23} {'Tanggal Lahir':<15} {'BEASISWA':<15}")
print("_"*80)
for data in siswa:
    KEY  = data
    NIS = siswa[KEY]["nis"]
    NAMA = siswa[KEY]["nama"]
    KELAS = siswa[KEY]["kelas"]
    TEMPAT_LAHIR = siswa[KEY]["tempat_lahir"]
    TANGGAL_LAHIR = siswa[KEY]["tgl_lahir"].strftime("%x")
    BEASISWA = siswa[KEY]["beasiswa"]
    print(f"{NIS:<14} {NAMA:^16} {KELAS:^15} {TEMPAT_LAHIR:^23} {TANGGAL_LAHIR:^15} {BEASISWA:^15}")
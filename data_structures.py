# List
angka = [1,2,3,4,5,6,7,8,9,10]
angka.append(11) # menambah data di akhir
angka.append(12)
angka.pop() # menghapus data terakhir
print(angka)
for x in range(10):
    print(x)
squares = []
squares = list(map(lambda x: x**2, range(10))) # menimpa variable yg yg masih ada pangkat dua dengan ekpresi lamda
lamda = [x**3 for x in range(10)] # pangkat tiga
gabungan = [(x,y) for x  in [1,3,4 ] for y in [3,5,6] if x != y] # gabungan data tidak sama
print("lamda pangkat dua")
print(squares)
print("lamda pangkat tiga")
print(lamda)
print("lamda  gabungan")
print(gabungan)


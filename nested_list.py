# append()	
# clear()	
# copy()	
# count()	
# extend()	    
# index()	
# insert()	
# pop()	 menghapus data dengan index (index)
# remove()	
# reverse()	
# sort()	
a = ["andi",12,"l"]
b = ["anto",14,"l"]
c = ["anti",10,"p"]
a_1 = [1,2]
a_2 = [2,3]
a_3 = [a_1,a_2]
list = [a,b,c]
for i in list:
    print(f"Nama\t: {i[0]}")
    print(f"Umur\t: {i[1]}")
    print(f"kel\t: {i[2]}\n")

list_copy = list.copy()
a[0] = "johan"
d = a.index("l") # index mengembaikan data index denagan kata kunci dalamnya (value)

# print(list)
# print(list_copy)
# print(f"Index ke: {d}")
print(a_3)
print(a_3[1][1]) # mengambil data list didalam list pastikan indext list pertama [0] dan index list didalanya index ke berpa yg mau di ambil [][]
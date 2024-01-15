a = set("please") # set tidak bisa mengambil nilai by index dan sasat pengambilan data akan teracak , cocok dengan perulangan method set menghapus data duplikat sama.
b = {a for a in "please"  if a not in 'e'} #menghapus huruf yg ada di dalam strings di type set
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print("apple di cetak sekali :")
for i in sorted(set(basket)):
    
    print(i, end=",")
print(a)
print(b)
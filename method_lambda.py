# output = argument:expression, sebelum argument ada lambda
import os

kuadrat = lambda angka:angka**2
kubik = lambda angka:angka**3
nama_list = ["andi","dia","zaki","az"]
nama_lambda = ["andi","dian","zak","ka"] #Note
lambbda = ["otong","ucup","dudung"]
angka = [1,2,3,4,5,6,7,8,9,10]
def kecil_lima(angka):
    return angka <5

list_angka = list(filter(kecil_lima,angka))
lambda_filter = list(filter(lambda x:x<7,angka))
lambda_modulus = list(filter(lambda x:x%2==0,angka))
nama_list.sort()
nama_lambda.sort(key=lambda nama:len(nama))
lambbda.sort(key=lambda nama:len(nama))
os.system("cls")

# print(f" Kuadrat :{kuadrat(3)}")
# print(f" Kubik :{kubik(3)}")
# print(f"Sort list {nama_list}")
# print(f"Sort pakai lambda {nama_lambda}")
# print(f"Sort  lambbda {lambbda}")

print(f"List filter :{list_angka}")
print(f"Lambda filter : {lambda_filter}")
print(f"Lambda Modulus : {lambda_modulus}")
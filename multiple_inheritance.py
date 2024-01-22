# Dapat mewarisi  1, 2 dan lebih class mengambil method yg berbeda
import os
class A:
    def set_team(self,a):
        self.a = a
    def show_team(self):
        print(f"Team :{self.a}")
        
class B:
    def set_type(self,b):
        self.b = b
    def show_type(self):
        print(f"Type :{self.b}")
    
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age
os.system("cls")
user = C("nita",31)
user.set_team("hijau")
user.set_type("kepiting")
user.show_team()
user.show_type()
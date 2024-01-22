# check dalam class dan method resolution order dan class lain
class A:
    
    def show(self):
        print("Team : A")
        
class B(A):
    
    def show(self):
        print("Type : B")
    
class C(A): 
    def show(self):
        print("Type : C")
class D(B,C): 
    pass

# os.system("cls")
objek = D()
objek.show()
help(objek)
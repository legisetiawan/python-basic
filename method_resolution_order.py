# Dapat mewarisi  1, 2 dan lebih class mempunyai method yg sama
# import os
class A:
    
    def show(self):
        print("Team : A")
        
class B:
    
    def show(self):
        print("Type : B")
    
class C(A,B): # urutan
    pass

# os.system("cls")

objek = C()
objek.show()
help(objek)
    
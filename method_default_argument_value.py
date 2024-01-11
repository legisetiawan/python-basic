def default_argument(name,age):
    print(f"Nama saya : {name} Umur : {age}")
default_argument("ani",46)

def default_value(name="Azis bin manaf",age=56,education="S1",vids=13):
    print(f"Nama saya : {name} Umur : {age}, Pendidikan Terakhir : {education}, Jumlah anak : {vids}")
default_value()

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
print(type(parrot(10)))
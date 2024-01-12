try:
    x = int(input("Masukan angka desimal: "))
    y = int(input("Masukan angka desimal : "))
    print(x / y)
except ValueError:
    print("Masukan bilangan yg valid")
except ZeroDivisionError:
    print("Data yg anda masukan tidak bisa di bagi nol")
    y = 1
    print(x/y)
finally:
    print("DONE")
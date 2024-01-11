#jika condisi tidak di penuhi akan mengulang code dan mengeksekusi code di luar kondisi if
for i in range(1,101):
    total = 0
    if i % 2 ==0:
        continue
    print(f"bilangan ganjil 1-100:",i)
# Odilio Ganesha Nugroho - 71210739
# Grup D Soal 3

a = int(input("Mauskkan bilangan pertama: "))
b = int(input("Mauskkan bilangan kedua: "))
c = int(input("Mauskkan bilangan ketiga: "))

if a > b and a > c:
    print('Yang terbesar adalah', a)
elif b > a and b > c:
    print('Yang terbesar adalah', b)
else:
    print('Yang terbesar adalah', c)

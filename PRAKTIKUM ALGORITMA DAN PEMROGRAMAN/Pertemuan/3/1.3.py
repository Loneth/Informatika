# Odilio Ganesha Nugroho - 71210739
# Grup A Soal 1.2

try:
    a = int(input('Masukkan bilangan pertama: '))
    b = int(input('Masukkan bilangan kedua: '))
    c = int(input('Masukkan bilangan ketiga: '))

    if a > b and a > c:
        print('Terbesar: ', a)
    elif b > a and b > c:
        print('Terbesar: ', b)
    elif c > a and c > b:
        print('Terbesar: ', c)
except ValueError:
    print('input yang anda masukkan salah!')

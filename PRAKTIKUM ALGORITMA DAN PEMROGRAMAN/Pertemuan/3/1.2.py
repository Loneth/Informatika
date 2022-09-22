# Odilio Ganesha Nugroho - 71210739
# Grup A Soal 1.2

try:
    bilangan = int(input('Masukkan suatu bilangan: '))
    if bilangan > 0:
        print('Positif')
    elif bilangan < 0:
        print('Negatif')
    elif bilangan == 0:
        print('Nol')
except ValueError:
    print('input yang anda masukkan salah!')

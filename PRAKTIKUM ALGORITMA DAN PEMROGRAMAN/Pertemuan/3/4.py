# Odilio Ganesha Nugroho - 71210739
# Grup A Soal 4

try:
    a = int(input('Masukkan sisi 1: '))
    b = int(input('Masukkan sisi 2: '))
    c = int(input('Masukkan sisi 3: '))

    if a == b == c:
        print('3 sisi sama')
    elif a == b or a == c or b == c:
        print('2 sisi sama')
    elif a != b != c:
        print('Tidak ada yang sama')
except ValueError:
    print('input yang anda masukkan tidak valid')

# Odilio Ganesha Nugroho - 71210739
# Grup A Soal 1

def cek_angka(a, b, c):
    if (a != b != c) and (a + b == c or b + c == a or c + a == b):
        return print('true')
    else:
        return print('false')


a = int(input('bilangan1 :'))
b = int(input('bilangan2 :'))
c = int(input('bilangan3 :'))

cek_angka(a, b, c)

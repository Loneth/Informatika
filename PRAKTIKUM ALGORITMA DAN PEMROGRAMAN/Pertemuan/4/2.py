def cek_digit_belakang(a, b, c):
    a = a % 10
    b = b % 10
    c = c % 10

    if a == b or b == c or c == a:
        return print('True')
    else:
        return print('False')


a = int(input('masukkan angka 1 : '))
b = int(input('masukkan angka 2 : '))
c = int(input('masukkan angka 3 : '))

cek_digit_belakang(a, b, c)

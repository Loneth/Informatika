# Odilio Ganesha Nugroho - 71210739
# Grup A Soal 1.1

try:
    suhu = int(input('Masukkan suhu tubuh: '))
    if suhu >= 38:
        print('Anda demam')
    else:
        print('Anda tidak demam')
except ValueError:
    print('input yang anda masukkan salah!')

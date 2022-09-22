# Odilio Ganesha Nugroho - 71210739
# Grup A Soal 3

try:
    a = int(input("Masukkan bulang 1-12 : "))

    if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
        hari = 31
    elif a == 4 or a == 6 or a == 9 or a == 11:
        hari = 30
    elif a == 2:
        hari = 29

    print("Jumlah hari :", hari)
except ValueError:
    print('input yang anda masukkan salah!')

# Odilio Ganesha Nugroho - 71210739
# Grup A Soal 2

a = int(input("Jumlah Jawaban Benar  : "))
b = int(input("Jumlah Jawaban Salah  : "))
c = int(input("Jumlah Jawaban kosong : "))

print("============REKAP NILAI============")
print("Jumlah Jawaban Benar  : ", a, "Soal")
print("Jumlah Jawaban Salah  : ", b, "Soal")
print("Jumlah Jawaban kosong : ", c, "Soal")

total_poin = (a * 3) + b
total_nilai = (total_poin / 90) * 100

print("Total Poin :", total_poin, "Poin")
print("Total Nilai :", round(total_nilai))

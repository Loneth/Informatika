# Odilio Ganesha Nugroho - 71210739
# Grup A Soal 1

print("===== INPUTAN =====")
a = int(input("Masukan uang mingguan : "))

bulan1 = int(input("Awal menabung pada bulan ke-"))
bulan2 = int(input("Akhir menabung pada bulan ke-"))

b = int(input("Masukan berapa persen untuk tabungan : "))
c = int(input("Masukan berapa persen untuk makan : "))
d = int(input("Masukan berapa persen untuk jajan : "))
e = int(input("Masukan berapa persen untuk kuliah : "))

print("========== Program Pengatur Keuangan ==========\n")
print("Uang bulanan : Rp", a)

x = bulan1 > 1 and bulan1 - 1 or 0
waktu = len(range(x, bulan2))

rumus1 = (waktu * 4) * a
rumus2 = (b / 100) * rumus1
rumus3 = (c / 100) * rumus1
rumus4 = (d / 100) * rumus1
rumus5 = (e / 100) * rumus1

print("Total uang yang didapat selama periode bulan", bulan1, "hingga", bulan2, ": Rp", rumus1)
print("uang untuk ditabung : Rp", rumus2)
print("Jatah uang untuk makan : Rp", rumus3)
print("Jatah uang untuk jajan : Rp", rumus4)
print("Jatah uang untuk kuliah : Rp", rumus5)

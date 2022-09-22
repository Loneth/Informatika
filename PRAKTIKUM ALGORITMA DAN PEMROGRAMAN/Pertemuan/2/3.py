# Odilio Ganesha Nugroho - 71210739
# Grup D Soal 3

a = int(input("Gaji per jam yang anda inginkan : "))
b = int(input("Jumlah jam kerja yang akan dilakukan dalam 1 minggu : "))

Jumlah_GajiKotor = a * b * 5
print(f"Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak : {'{:,.2f}'.format(Jumlah_GajiKotor)}")

Jumlah_Pajak = Jumlah_GajiKotor * (14 / 100)
Jumlah_GajiBersih = Jumlah_GajiKotor - Jumlah_Pajak
print(f"Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak : {'{:,.2f}'.format(Jumlah_GajiBersih)}")

Baju = Jumlah_GajiBersih * (10 / 100)
print(f"Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris : {'{:,.2f}'.format(Baju)}")

Alat_Tulis = Jumlah_GajiBersih * (1 / 100)
print(f"Jumlah uang yang akan Budi habiskan untuk membeli alat tulis : {'{:,.2f}'.format(Alat_Tulis)}")

UangSedekah = (Jumlah_GajiBersih - Baju - Alat_Tulis) * (25 / 100)
print(f"Jumlah uang yang akan Budi sedekahkan : {'{:,.2f}'.format(UangSedekah)}")

Untuk_Anak_Yatim = (UangSedekah // 1000) * 1000 * (30 / 100)
print(f"Jumlah uang yang akan diterima anak yatim : {'{:,.2f}'.format(Untuk_Anak_Yatim)}")

Untuk_Kaum_duafa = UangSedekah - Untuk_Anak_Yatim
print(f"Jumlah uang yang akan diterima kaum dhuafa : {'{:,.2f}'.format(Untuk_Kaum_duafa)}")

Sisa_UangSedekah = Jumlah_GajiBersih - UangSedekah - Baju - Alat_Tulis
print(f"Sisa uang Budi adalah : {'{:,.2f}'.format(Sisa_UangSedekah)}")

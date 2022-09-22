a = input("Masukan pendapatan perusahan : ")
b = input("Masukan jumlah barang mewah : ")
c = input("Masukan tahun didirikan : ")

a = int(a)
b = int(b)
c = int(c)

if c < 2000 or a < 500_000_000:
    pajak = 0.10
elif (c > 2000 and c <= 2010 and b == 0) or (a > 500_000_000 and a <= 1_000_000_000):
    pajak = 0.20
elif b > 10 or (c > 2010 and a > 1_000_000_000):
    pajak = 0.50
else:
    pajak = 0

ya = pajak * a
print(f"Pajak yang harus di bayar oleh perusahaan Rp.{ya}")

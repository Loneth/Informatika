bulan1 = int(input("Awal menabung pada bulan ke-"))
bulan2 = int(input("Akhir menabung pada bulan ke-"))

b = bulan1 > 1 and bulan1 - 1 or 0
# b = bulan1 if bulan1 > 1 else 0

waktu = len(range(b, bulan2))

for i in range(b, bulan2):
    print(i, end=" ")

# if bulan1 > 1:
#     waktu = range(1, bulan2, 0)[-1]
# else:
#     waktu = range(bulan1, bulan2)[-1]

print("\nLast element:", waktu)

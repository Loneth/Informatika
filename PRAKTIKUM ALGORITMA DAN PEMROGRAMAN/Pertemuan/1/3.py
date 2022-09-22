P = 200000000
r = 0.1
n = 1

t = 0
while P < 400000000:
    P = P + (P * r)
    t += 1

print(f"Uangnya Erika menjadi Rp. {'{:,.2f}'.format(int(P))}, Waktu yang dibutuhkan adalah {t} tahun.")

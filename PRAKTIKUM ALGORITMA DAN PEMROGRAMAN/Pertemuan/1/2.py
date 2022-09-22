emas = 25
harga_pertama = 650000
harga_kedua = 685000
modal_pertama = harga_pertama * emas

a = (harga_kedua - harga_pertama) * emas
b = (a / modal_pertama) * 100

print("Keuntungan yang didapat oleh Gerard :")
print(f"- Rp. {'{:,}'.format(a)}")
print(f"- {round(b)}%")

emas2 = 15
harga_ketiga = 715000
modal_kedua = harga_kedua * emas2

c = (harga_ketiga - harga_kedua) * emas2
d = (c / modal_kedua) * 100

print("Jika Gerard kemudian membeli lagi 15 gram emas dengan harga Rp. 685.000, kemudian harga emas naik lagi "
      "menjadi Rp. 715.000 :")
print(f"- Rp. {'{:,}'.format(c)}")
print(f"- {round(d)}%")


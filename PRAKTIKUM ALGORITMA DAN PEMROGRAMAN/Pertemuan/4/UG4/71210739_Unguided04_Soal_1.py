def move(x: int, y: int, arah: str, langkah: int = 5):
    x1 = x
    y1 = y

    if arah == "barat":
        x1 = x - langkah
    elif arah == "selatan":
        y1 = y - langkah
    elif arah == "timur":
        x1 = langkah - x
    elif arah == "utara":
        y1 = langkah - y
    else:
        return "Anda salah arah"

    print(f"Pergi ke arah {arah} sejauh {langkah} langkah dari titik awal x:{x}, y:{y} menuju ke x:{x1}, y:{y1}")


move(1, 2, "timur", 5)

def move(x: int, y: int, arah: str, langkah: int = 5):
    x1 = x
    y1 = y

    if arah == "barat":
        x1 = x - langkah
    elif arah == "selatan":
        y1 = y - langkah
    else:
        return "Anda salah arah"

    print(f"Pergi ke arah {arah} sejauh {langkah} langkah dari titik awal x:{x}, y:{y} menuju ke x:{x1}, y:{y1}")


move(5, 5, "selatan")

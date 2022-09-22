try:
    a = input("Masukkan jumlah jam kerja dalam seminggu : ")
    b = input("Masukkan posisi anda (Manager/Supervisor/Staff) : ")
    c = input("Masukkan jumlah jam lembur dalam seminggu : ")

    a = int(a)
    b = str(b)
    c = int(c)

    # pesan = ""
    if a > 12 and a <= 30:
        gaji = a * 10000
    elif a > 30 and a < 70:
        gaji = a * 15000
    elif a >= 70:
        gaji = a * 20000
    else:
        gaji = 0
        print("Inputan Anda tidak sesuai")

    if b == "Manager":
        tunjangan = 5000000
    elif b == "Supervisor":
        tunjangan = 3000000
    elif b == "Staff":
        tunjangan = 2000000
    else:
        tunjangan = 0
        print("Posisi Anda tidak mendapatkan tunjangan")

    if c >= 6 and c <= 8:
        lembur = c * 5000
    elif c > 8 and c < 12:
        lembur = c * 10000
    elif c >= 12:
        lembur = c * 15000
    else:
        lembur = 0
        print("Jam lembur tidak sesuai ketentuan")

    print("\n====================PERHITUNGAN GAJI====================")
    print("Gaji Pokok : Rp", gaji)
    print("Tunjangan : Rp", tunjangan)
    print("Lembur : Rp", lembur)
except:
    print("Inputan Anda Tidak sesuai")

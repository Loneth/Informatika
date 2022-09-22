def nilai_huruf(nilaiTotal):
    if nilaiTotal > 85:
        nilaiHuruf = "A"
    elif 80 <= nilaiTotal <= 84:
        nilaiHuruf = "A-"
    elif 75 >= nilaiTotal <= 79:
        nilaiHuruf = "B+"
    elif 70 >= nilaiTotal <= 74:
        nilaiHuruf = "B"
    elif 65 >= nilaiTotal <= 69:
        nilaiHuruf = "B-"
    elif 60 >= nilaiTotal <= 64:
        nilaiHuruf = "C+"
    elif 55 >= nilaiTotal <= 59:
        nilaiHuruf = "C"
    elif 45 >= nilaiTotal <= 54:
        nilaiHuruf = "D"

    return nilaiHuruf


def nilai_akhir(uts, uas, tugas):
    uts = int(uts)
    uas = int(uas)
    tugas = int(tugas)

    nilaiUTS = uts * 35 / 100
    nilaiUAS = uas * 35 / 100
    nilaiTugas = tugas * 30 / 100
    nilaiTotal = nilaiUTS + nilaiUAS + nilaiTugas

    return nilaiTotal


try:
    print("========== Data Nilai ==========")
    a = input("Masukkan Nilai UTS \t\t: ")
    b = input("Masukkan Nilai UAS \t\t: ")
    c = input("Masukkan Nilai Tugas \t: ")

    nilai_akhir(a, b, c)

    print("\n========== Nilai Mahasiswa ==========")
    d = nilai_akhir(a, b, c)
    print(f"Nilai Akhir Mahasiswa \t: {float(d)}")
    e = nilai_huruf(d)
    print(f"Nilai Huruf Mahasiswa \t: {e}")
except ValueError:
    print("\n========== Nilai Mahasiswa ==========")
    print("Data Anda Salah")

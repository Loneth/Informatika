def nilai_akhir(uts, uas, tugas):
    print("\n========== Nilai Mahasiswa ==========")
    uts = int(uts)
    uas = int(uas)
    tugas = int(tugas)

    nilaiUTS = uts * 35 / 100
    nilaiUAS = uas * 35 / 100
    nilaiTugas = tugas * 30 / 100
    nilaiTotal = nilaiUTS + nilaiUAS + nilaiTugas

    print(f"Nilai Akhir Mahasiswa \t: {float(nilaiTotal)}")


try:
    print("========== Data Nilai ==========")
    a = input("Masukkan Nilai UTS \t\t: ")
    b = input("Masukkan Nilai UAS \t\t: ")
    c = input("Masukkan Nilai Tugas \t: ")

    nilai_akhir(a, b, c)
except ValueError:
    print("Data Anda Salah")

buku = {
    "buku1": {
        "judul": "pengetahuan bontang",
        "penulis": "fery",
        "tahun_terbit": "2017"
    },

    "buku2": {
        "judul": "beli mobil 20rb",
        "penulis": "omar",
        "tahun_terbit": "2026"
    },

    "buku3": {
        "judul": "cara memahami perempuan",
        "penulis": "jikir",
        "tahun_terbit": "2020"
    }
}

while True:
    print("===== DATA BUKU =====")
    print("1. tampilkan data buku")
    print("2. tambah penerbit")
    print("3. ubah penulis")
    print("4. hapus penerbit")
    print("5. tampilkan data setelah perubahan")
    print("6. keluar")
    print("=====================")

    pilihan = input("pilih menu (1-6): ")

    if pilihan == "1":
        print("===== DATA BUKU =====")

        print("Buku 1")
        print("judul:", buku["buku1"]["judul"])
        print("penulis:", buku["buku1"]["penulis"])
        print("tahun_terbit:", buku["buku1"]["tahun_terbit"])

        if "penerbit" in buku["buku1"]:
            print("penerbit:", buku["buku1"]["penerbit"])

        print("Buku 2")
        print("judul:", buku["buku2"]["judul"])
        print("penulis:", buku["buku2"]["penulis"])
        print("tahun_terbit:", buku["buku2"]["tahun_terbit"])

        if "penerbit" in buku["buku2"]:
            print("penerbit:", buku["buku2"]["penerbit"])

        print("Buku 3")
        print("judul:", buku["buku3"]["judul"])
        print("penulis:", buku["buku3"]["penulis"])
        print("tahun_terbit:", buku["buku3"]["tahun_terbit"])

        if "penerbit" in buku["buku3"]:
            print("penerbit:", buku["buku3"]["penerbit"])

    elif pilihan == "2":
        print("===== TAMBAH PENERBIT =====")

        penerbit1 = input("Masukkan penerbit buku 1: ")
        buku["buku1"]["penerbit"] = penerbit1

        penerbit2 = input("Masukkan penerbit buku 2: ")
        buku["buku2"]["penerbit"] = penerbit2

        penerbit3 = input("Masukkan penerbit buku 3: ")
        buku["buku3"]["penerbit"] = penerbit3

        print("Data penerbit berhasil ditambahkan.")

    elif pilihan == "3":
        print("===== UBAH PENULIS =====")

        penulis1 = input("Masukkan penulis baru buku 1: ")
        buku["buku1"]["penulis"] = penulis1

        penulis2 = input("Masukkan penulis baru buku 2: ")
        buku["buku2"]["penulis"] = penulis2

        penulis3 = input("Masukkan penulis baru buku 3: ")
        buku["buku3"]["penulis"] = penulis3

        print("Data penulis berhasil diubah.")

    elif pilihan == "4":
        print("===== HAPUS PENERBIT =====")
        print("1. Buku 1")
        print("2. Buku 2")
        print("3. Buku 3")

        nomor = input("Pilih buku yang ingin dihapus penerbitnya (1-3): ")

        if nomor == "1":
            if "penerbit" in buku["buku1"]:
                del buku["buku1"]["penerbit"]
                print("Penerbit buku 1 berhasil dihapus.")
            else:
                print("Penerbit buku 1 belum tersedia.")

        elif nomor == "2":
            if "penerbit" in buku["buku2"]:
                del buku["buku2"]["penerbit"]
                print("Penerbit buku 2 berhasil dihapus.")
            else:
                print("Penerbit buku 2 belum tersedia.")

        elif nomor == "3":
            if "penerbit" in buku["buku3"]:
                del buku["buku3"]["penerbit"]
                print("Penerbit buku 3 berhasil dihapus.")
            else:
                print("Penerbit buku 3 belum tersedia.")

        else:
            print("Nomor buku tidak tersedia.")

    elif pilihan == "5":
        print("===== DATA BUKU SETELAH PERUBAHAN =====")

        print(buku)

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan menu tidak valid.")
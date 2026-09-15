# Studi_Kasus_4_Fery-Sugiantoro_2609116039

Merupakan program sederhana menggunakan Python untuk menyimpan dan mengelola data buku. Program ini menggunakan dictionary untuk menyimpan informasi seperti judul, penulis, tahun terbit, dan penerbit.

Program memiliki beberapa menu, yaitu menampilkan data buku, menambah penerbit, mengubah penulis, menghapus penerbit, menampilkan data setelah perubahan, dan keluar dari program.

Fitur Program

1. Menampilkan data buku.
2. Menambah penerbit untuk setiap buku.
3. Mengubah nama penulis setiap buku.
4. Menghapus penerbit dari buku yang dipilih.
5. Menampilkan data buku setelah perubahan.
6. Keluar dari program.

Penjelasan Kode Program

1. Dictionary "buku"

buku = {
    "buku1": {
        "judul": "pengetahuan bontang",
        "penulis": "jikir",
        "tahun_terbit": "2017"
    }
}

Digunakan untuk menyimpan data buku dalam bentuk dictionary. Setiap buku memiliki data judul, penulis, dan tahun terbit.

2. Perulangan "while True"

while True:

Digunakan agar menu program terus ditampilkan dan dapat digunakan berulang kali sampai pengguna memilih menu keluar.

3. Input dan Pilihan Menu

pilihan = input("pilih menu (1-6): ")

Digunakan untuk menerima pilihan menu dari pengguna.

4. Percabangan "if", "elif", dan "else"

Digunakan untuk menjalankan perintah sesuai pilihan menu. Contohnya, pilihan 1 untuk menampilkan data buku dan pilihan 2 untuk menambah penerbit.

5. Menambah dan Mengubah Data

buku["buku1"]["penerbit"] = penerbit1

Digunakan untuk menambahkan data penerbit ke buku.

buku["buku1"]["penulis"] = penulis1

Digunakan untuk mengubah nama penulis buku.

6. Percabangan Pengecekan "in"

if "penerbit" in buku["buku1"]:

Digunakan untuk mengecek apakah data penerbit sudah tersedia di dalam buku.

7. Menghapus Data dengan "del"

del buku["buku1"]["penerbit"]

Digunakan untuk menghapus data penerbit dari buku yang dipilih.

8. Menampilkan Data dengan "print()"

print(buku)

Digunakan untuk menampilkan seluruh data buku setelah perubahan.

9. "break"

break

Digunakan untuk menghentikan perulangan "while True" ketika pengguna memilih menu keluar.

Kesimpulan

Program Data Buku Python dapat digunakan untuk mengelola data buku sederhana. Program ini menerapkan dictionary, perulangan, percabangan, input, dan operasi penambahan, perubahan, serta penghapusan data.

# screenshot output

<img width="1501" height="950" alt="Screenshot 2026-09-15 210247" src="https://github.com/user-attachments/assets/c539d7e0-6301-49fd-bc77-fa343c332bdb" />

<img width="1481" height="988" alt="Screenshot 2026-09-15 210313" src="https://github.com/user-attachments/assets/b0d6a661-73d6-4a01-8f64-ecb0ea4ed6ef" />

<img width="1476" height="435" alt="Screenshot 2026-09-15 210412" src="https://github.com/user-attachments/assets/0a17eef1-9f6d-4041-88ab-35d1cb26702f" />


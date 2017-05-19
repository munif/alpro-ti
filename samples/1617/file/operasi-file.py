# Cara membaca file sama seperti membaca buku
# 1. Buka <- nama file
# 2. Dibaca atau ditulis
# 3. Ditutup

# Cara membuka file menggunakan open()
file1 = open("D:\\coba.txt", "r")

# Untuk Mac
import os
f = open(os.path.expanduser("~/Desktop/file.txt"), "r")

# Membaca file
# 1. Membaca semua
file1.read()

# 2. Membaca baris pertama
file1.readline()

# 3. Membaca semua baris dan dimasukkan ke list
isi_file = file1.readlines()

# 4. Menggunakan looping
data = []
for line in file1:
    data.append(line)

# Menutup file
file1.close()
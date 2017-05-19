"""
Cara membaca file dari csv
"""

import csv 
 
""" Sesuaikan di mana lokasi file kalian berada. Gunakan tanda \\ untuk memisahkan struktur folder"""
f = open("D:\\repo\\alpro-ti\\exercises\\15\\data.csv", "rb")

""" Untuk membaca file, gunakan reader """
reader = csv.reader(f)

""" Memasukkan hasil pembacaan ke dalam variabel data dalam bentuk list """
data = list(reader)

""" print isi dari variabel data """
print(data)

""" Contoh mengakses data baris kedua, kolom pertama """
print(data[1][0])

f.close()


"""
Catatan:
Baris pertama merupakan header dari tabel sehingga biasanya tidak diikutkan dalam pengolahan data
"""
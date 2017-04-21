"""
Materi list dapat dilihat di:
https://docs.python.org/2/tutorial/datastructures.html
"""

# Input jumlah mahasiswa
jml_mhs = input('Masukkan jumlah mahasiswa: ')

# Deklarasi array terlebih dahulu
usia = []
for i in range(0, jml_mhs):
    # Meminta input dari user dan dimasukkan
    # ke dalam array
    usia.append(input('Masukkan usia: '))
    
# Hitung total usianya
total_usia = 0

for i in range(0, len(usia)):
    total_usia = total_usia + usia[i]
    
# Hitung rata-rata usia
rata_rata = total_usia / float(jml_mhs)

print "Rata-rata usia adalah %f" % rata_rata
    
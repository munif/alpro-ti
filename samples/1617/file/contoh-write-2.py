nama = ['Andi', 'Bambang', 'Cici']
nilai1 = [80, 70, 60]
nilai2 = [90, 90, 70]
nilai3 = [90, 75, 70]

# Simpan dengan format seperti ini
# Andi, 80, 90, 90
# Bambang, 70, 90, 75
# Cici, 60, 70, 70

f = open("D:\\nilai.txt", "w")

for i in range(0, 3):
    f.write(nama[i] + "," + 
            str(nilai1[i]) + "," + 
            str(nilai2[i]) + "," + 
            str(nilai3[i]) + "\n")

f.close()

# Fungsi menghitung rata-rata 3 bilangan
def frata_rata(a, b, c):
    jumlah = a + b + c
    return jumlah/3.0

f = open("D:\\rata_rata.txt", "w")
for i in range(0, 3):
    rata = frata_rata(nilai1[i], nilai2[i], nilai3[i])
    f.write(nama[i] + "," + str(rata) + "\n")
    
f.close()
    
    
    
    
    
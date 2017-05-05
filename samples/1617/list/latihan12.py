# Soal 1
n = input('Masukkan panjang array-nya: ')
arr = []

for i in range (0, n):
    arr.append(input())
    
arrcount = []
for i in range(0, n):
    arrcount.append(arr.count(arr[i]))

for i in range(0, n):
    if arrcount[i] == 1:
        print arr[i],
    

# Soal 2
n = input('Masukkan panjang array-nya: ')
arr = []
for i in range(0, n):
    arr.append(input())

print arr

m = input('Masukkan jumlah rotasinya: ')
if len(arr) % 2 == 0:
    for i in range(m, n):
        temp = arr[i-m]
        arr[i-m] = arr[i]
        arr[i] = temp   
else:
    for i in range(m, n):
        temp = arr[i-m]
        arr[i-m] = arr[i]
        arr[i+1] = temp

print arr
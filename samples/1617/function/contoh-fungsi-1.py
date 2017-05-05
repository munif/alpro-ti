def nilai_absolut(x):
    if x < 0:
        return x * -1
    else:
        return x

def tabel_perkalian(x, y, z):
    for i in range (y, z + 1):
        hasil = x * i
        print "%d x %d = %d" %(x, i, hasil)


a = input("Masukkan angka: ")
b = input("Masukkan batas bawah: ")
c = input("Masukkan batas atas: ")
        
tabel_perkalian(a, b, c)


## Soal 2

def faktorial(n):
    # Tambahkan untuk fungsi faktorial
    hasil = 1
    for i in range(1, n+1):
        hasil = hasil * i
    return hasil

def c(n, r):
    return faktorial(n)/(faktorial(n-r)*faktorial(r))

def p(n, r):
    return faktorial(n)/faktorial(n-r)

c(5, 3)
p(5, 3)


## Soal 3
## Mencari akar persamaan kuadratik
## menggunakan rumus ABC

import math
def rumus_abc(a, b, c):
    det = b**2 - 4*a*c
    if det < 0:
        print "Determinant less than 0, cannot calculate."
        return None, None
    else:
        x1 = (-b + math.sqrt(det))/(2*a)
        x2 = (-b - math.sqrt(det))/(2*a)
        return x1, x2
    

x1, x2 = rumus_abc(1.0, 3.0, -4.0)
x1, x2 = rumus_abc(4, -4.0, 4)

# 2 data jadi 1 variabel -> tuple
x = rumus_abc(1.0, 3.0, -4.0)
















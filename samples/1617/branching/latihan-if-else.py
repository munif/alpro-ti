"""
Soal-soal diambil dari:
    http://www.codeforwin.in/2015/05/if-else-programming-practice.html
"""

# 1. Nilai maksimum dari dua buah bilangan
a = input('Masukkan bilangan pertama: ')
b = input('Masukkan bilangan kedua: ')
if a > b:
    print 'a is larger than b.'
elif a < b:
    print 'b is larger than a.'
elif a == b:
    print 'a and b are equal'

# 2. Maksimum dari tiga bilangan
a = input('Masukkan bilangan pertama: ')
b = input('Masukkan bilangan kedua: ')
c = input('Masukkan bilangan ketiga: ')
if a > b:
    if a > c:
        print 'a is the largest'
    elif a < c:
        print 'c is the largest'
    elif a == c:
        print 'a and c are equal'
elif a < b:
    if b > c:
        print 'b is the largest'
    elif b < c:
        print 'c is the largest'
    elif b == c:
        print 'b and c are equal'
elif a == b:
    if b > c:
        print 'a and b is the largest'
    elif b < c:
        print 'c is the largest'
    elif b == c:
        print 'a, b, and c are equal'

print 'Program nomor 2 selesai'

# 3. Menentukan tahun kabisat

tahun = input('Masukkan tahun: ')
# Step 1
if tahun % 4 == 0:
    # Step 2
    if tahun % 100 == 0:
        # Step 3
        if tahun % 400 == 0:
            # Step 4
            print 'is a leap year'
        else:
            print 'not a leap year'
    else:
        # Step 4
        print 'is a leap year'
# Step 5
else:
    print 'Not a leap year'

# 4. Menentukan jenis segitiga
#    Ada 3 jenis:
#    1. equilateral: sama sisi
#    2. isosceles: sama kaki
#    3. scalene: tidak beraturan
a = input ('Masukkan sisi pertama: ')
b = input ('Masukkan sisi kedua: ')
c = input ('Masukkan sisi ketiga: ')

if a == b:
    if b == c:
        print 'Equilateral'
    else:
        print 'Isosceles'
elif a != b:
    if b == c:
        print 'Isosceles'
    elif a == c:
        print 'Isosceles'
    elif b != c:
        print 'Scalene'
        
# 4. Algoritma yang kedua
a = input ('Masukkan sisi pertama: ')
b = input ('Masukkan sisi kedua: ')
c = input ('Masukkan sisi ketiga: ')

if a == b and b == c:
    print 'Equilateral'
elif a == b or b == c or a == c:
    print 'Isosceles'
else:
    print 'Scalene'


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








        
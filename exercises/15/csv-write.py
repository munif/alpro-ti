"""
Cara menulis data ke dalam file csv
"""

# Pustaka untuk operasi file CSV
import csv 
 
f = open("D:\\repo\\alpro-ti\\exercises\\15\\data-output.csv", "wb")

""" Untuk menulis ke dalam file, gunakan writer """
writer = csv.writer(f)

""" Misalkan ada data dalam bentuk list seperti ini """
data = [[1, 2], [3, 4], [5, 6]]

# Menuliskan header
writer.writerow(['x', 'y'])

for i in range(0, len(data)):
    """ Fungsi writerow() hanya menerima input dalam bentuk list.
        Oleh karena itu jangan lupa menuliskan kurung siku di dalamnya."""
    writer.writerow([ data[i][0], data[i][1] ])
    
f.close()
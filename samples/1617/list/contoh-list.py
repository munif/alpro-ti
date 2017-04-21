usia = [19, 20, 21, 18, 17, 19, 19, 18, 19, 18]

jumlah_data = len(usia)

total_usia = 0

for i in range(0, len(usia)):
    total_usia = total_usia + usia[i]

rata_rata_usia = total_usia / float(jumlah_data)


f = open("D:\\data.txt", "w")
f.write("Selamat siang\n")
f.write("Bukan, selamat sore.\n")
f.write("Kalimat ketiga.")

f.close()

# Contoh 2

data = []
for i in range(1, 11):
    data.append(i)

f = open("D:\\data.txt", "w")

for i in range (0, len(data)):
    f.write(str(data[i]) + "\n")

f.close()
f = open("D:\\rata_rata.txt", "r")
for i in f:
    data = i.split(",")
    data[1] = float(data[1])
    print data
    
f.close()
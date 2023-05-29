
kBarang = []
nBarang = []
hBarang = []
kBarang.append("001")
kBarang.append("002")
kBarang.append("003")
nBarang.append("tes tes ji")
nBarang.append("tes ji")
nBarang.append("tes")
hBarang.append(5000)
hBarang.append(500000)
hBarang.append(50000)
for i in range (len (kBarang)):
    print(i+1," ", kBarang[i], "       ", nBarang[i].ljust(15)," ",str(hBarang[i]).rjust(6))
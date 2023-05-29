#Program untuk menentukan harga dan bonus

#pembelian a=barang elektronik
#tampilan:

nama_barang = input("Masukkan nama barang:")
jumlah_barang = int(input("Masukkan jumlah barang:"))

if(nama_barang == "Kulkas"):
    hBarang = 2000000
    bonus = "kipas angin"
elif(nama_barang == "Televisi"):
    hBarang = 1500000
    bonus = "speaker"
elif(nama_barang == "Mesin Cuci"):
    hBarang = 3000000
    bonus = "rice cooker"
elif(nama_barang == "Laptop"):
    hBarang = 5000000
    bonus = "mouse wireless"
print("Harga barang:", hBarang)
total_bayar = hBarang * jumlah_barang
print("Total bayar:", total_bayar) 
print("Bonus:", bonus)

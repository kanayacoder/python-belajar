#KanayaMart
print("Selamat datang di KanayaMart")
total_harga = 0
lagi = "y"
while (lagi == "y") :
    nama_barang = ""
    hBarang = 0
    kode_barang = input("Masukkan kode barang:")
    
    if(kode_barang == "001"):
        nama_barang = "Indomie Goreng"
        hBarang = 3000
    elif(kode_barang == "002"):
        nama_barang = "Sabun Zen"
        hBarang = 5000
    elif(kode_barang == "003"):
        nama_barang = "Sampho Sunsilk"
        hBarang = 500
    elif(kode_barang == "004"):
        nama_barang = "Roti Tawar"
        hBarang = 15000
    elif(kode_barang == "005"):
        nama_barang = "Taro"
        hBarang = 10000
    print("Nama Barang:", nama_barang)
    print("Harga barang:", hBarang)
    jumlah_barang = int(input("Masukkan jumlah barang:"))
    subTotal = hBarang * jumlah_barang
    print("Sub total adalah:", subTotal)
    total_harga += subTotal
    lagi=input("Masih ada lagi? (y/t):")
print("Total Harga adalah:", total_harga)
jumlah_uang = int(input("Masukkan jumlah uang Anda:"))
uang_kembalian = jumlah_uang - total_harga
print("Ini uang kembalian anda:",uang_kembalian)
print("Terima Kasih Telah Berbelanja Selamat Datang Kembali :) by Kanaya")


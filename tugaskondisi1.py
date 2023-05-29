#Program untuk menghitung kasir gadde gadde
lagi = "y"
while (lagi == "y") :
    diskon = 0
    hargabarang1 =int(input("Masukkan harga barang1:"))
    hargabarang2 =int(input("Masukkan harga barang2:"))
    hargabarang3 =int(input("Masukkan harga barang3:"))
    totalharga = hargabarang1 + hargabarang2 + hargabarang3
    print("Total harga adalah:", totalharga)
    if(totalharga > 100000):
        diskon = totalharga * 10/100
    print("Potongan diskon adalah:",diskon)
    totalbayar = totalharga - diskon
    print("Total bayar adalah:",totalbayar)
    jumlahuang = int(input("Masukkan jumlah uang Anda:"))
    uangkembalian = jumlahuang - totalbayar
    print("Uang kembalian adalah:",uangkembalian)
    lagi=input("Masih mau lagi? (y/t):")
print("Terima Kasih Telah Berbelanja :) by Kanaya")

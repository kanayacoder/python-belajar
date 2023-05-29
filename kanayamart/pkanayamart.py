import mkanayamart as mkm
pil = 0
kBarang = []
nBarang = []
hBarang = []
tkBarang = []
tnBarang = []
thBarang = []
tJumlah = []
tsubTotal = []   
while(pil!=5):
    pil = mkm.menu()
    if(pil == 1):
        lagi = "y"
        kodebrg = ""
        namabrg = ""
        hargabrg = 0
        while (lagi == "y") :
            kodebrg = input("Masukkan kode barang:")
            namabrg = input("Massukan nama barang:")
            hargabrg = int(input("Massukan harga barang: "))
            kBarang.append(kodebrg)
            nBarang.append(namabrg)
            hBarang.append(hargabrg)
            lagi=input("Masih ada lagi? (y/t):")
    elif(pil == 2):
        print("no kode barang nama barang        harga barang ")
        for i in range (len (kBarang)):
            print(i+1," ", kBarang[i], "       ", nBarang[i].ljust(20)," ",str(hBarang[i]).rjust(6))
    elif(pil == 3):
        print("Selamat datang di KanayaMart")
        total_harga = 0
        lagi = "y"
        while (lagi == "y") :
            kode_barang = input("Masukkan kode barang:")
            i = kBarang.index(kode_barang)
            print("Nama Barang:", nBarang[i])
            print("Harga barang:", hBarang[i])
            jumlah_barang = int(input("Masukkan jumlah barang:"))
            subTotal = hBarang[i] * jumlah_barang
            print("Sub total adalah:", subTotal)
            total_harga += subTotal
            tkBarang.append(kBarang[i])
            tnBarang.append(nBarang[i])
            thBarang.append(hBarang[i])
            tJumlah.append(jumlah_barang)
            tsubTotal.append(subTotal)
            lagi=input("Masih ada lagi? (y/t):")
        print("Total Harga adalah:", total_harga)
        jumlah_uang = int(input("Masukkan jumlah uang Anda:"))
        uang_kembalian = jumlah_uang - total_harga
        print("Ini uang kembalian anda:",uang_kembalian)
        print("Terima Kasih Telah Berbelanja Selamat Datang Kembali :) by Kanaya")
    elif(pil == 4):
        print("no kode barang nama barang        harga barang jumlah   subtotal ")
        for i in range (len (tkBarang)):
            total_harga += tsubTotal[i]
            print(i+1," ", tkBarang[i], "       ", tnBarang[i].ljust(20)," ",str(thBarang[i]).rjust(6)," ", str(tJumlah[i]).rjust(2), "     ", str(tsubTotal[i]).rjust(6))
        print("                                total transaksi:", total_harga )
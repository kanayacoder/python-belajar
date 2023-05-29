# Aplikasi Menghitung Luas Dan Keliling Bidang Datar
import modulbdatar as mbd
mbd.judul()
lagi = "y"
while(lagi == "y"):
    mbd.menu()
    pilih = int(input("Masukkan pilihan (1,2 atau 3):"))
    if(pilih == 1):
        panjang = int(input("Massukan nilai panjang:"))
        lebar = int(input("Massukan nilai lebar:"))
        print("Luas persegi adalah:", mbd.lpersegi(panjang,lebar))
        print("Keliling persegi adalah:", mbd.kpersegi(panjang,lebar))
    elif(pilih == 2):
        alas = int(input("Massukan nilai alas/sisi bawah:"))
        tinggi = int(input("Massukan nilai tinggi:"))
        skiri = int(input("Massukan sisi kiri:"))
        skanan = int(input("Massukan sisi kanan:"))
        print("Luas segitiga adalah:", mbd.lsegitiga(alas,tinggi))
        print("Keliling segitiga adalah:", mbd.ksegitiga(alas,skiri,skanan))
    elif(pilih == 3):
        jarijari = int(input("Massukan nilai jari jari:"))
        mbd.lklingkaran(jarijari)
    else:print("Maaf, pilihan menu tidak tersedia")
    lagi=input("Masih mau lagi? (y/t):")
mbd.terimakasih()
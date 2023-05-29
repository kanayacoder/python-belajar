#Menghitung luas dan keliling lingkaran 
import math
print("Aplikasi Menghitung Luas Dan Keliling Lingkaran")
lagi = "y"
while(lagi == "y"):
    jarijari = int(input("masukkan nilai jarijari:"))
    luas = math.pi * jarijari * jarijari
    keliling = 2 * math.pi * jarijari
    print("Luas lingkaran adalah:",luas)
    print("Keliling lingkaran adalah:",keliling)
    lagi=input("Masih mau lagi? (y/t):")
print("Terima Kasih Telah Menggunakan Aplikasi Ini :) by Kanaya")


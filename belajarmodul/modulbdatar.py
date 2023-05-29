#Modul Aplikasi Menghitung Luas Dan Keliling Bidang Datar
import math
def judul():
    print("Aplikasi Menghitung Luas Dan Keliling Bidang Datar")
    print("Persegi,Segitiga atau Lingkaran")
    return
def lpersegi(p,l):
    luas = p*l
    return luas
def kpersegi(p,l):
    keliling = 2*p+2*l
    return keliling
def lsegitiga(a,t):
    luas = 0.5*a*t
    return luas
def ksegitiga(a,b,c):
    keliling = a+b+c
    return keliling
def lklingkaran(r):
    luas = math.pi*r*r
    keliling = 2*math.pi*r
    print("Luas lingkaran adalah:", luas )
    print("Keliling lingkaran adalah:", keliling)
    return  
def terimakasih():
    print("Terima Kasih Telah Menggunakan Aplikasi Ini :) by Kanaya")
    return
def menu():
    print("1. persegi")
    print("2. segitiga")
    print("3. lingkaran")
    return
    
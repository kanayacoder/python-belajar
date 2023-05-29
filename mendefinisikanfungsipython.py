'''
def printme(str):
    "This prints a passed string into this  function"
    print (str)
    return

printme("Hello World")
'''
def luass3(a,t):
    l = 0.5 * a * t
    return l
#Menghitung luas segitiga
print("Aplikasi Menghitung Luas Segitiga")

alas = int(input("masukkan nilai alas:"))
tinggi = int(input("masukkan nilai tinggi:"))
print("Luas persegi panjang adalah:",luass3(alas,tinggi))

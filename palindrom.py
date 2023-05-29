kata = input("kata:")
panjang = len(kata)
i = panjang - 1
kata2 = ""
while (i >=0):
    kata2 += kata[i]
    #print(kata[i],end="")
    i -= 1
if (kata2==kata):
    print("palindrom")
else:
    print("bukan polindrom")
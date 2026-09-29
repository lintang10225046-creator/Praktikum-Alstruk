#Input bilangan bulat dari pengguna
n = int(input("Masukkan bilangan: "))

is_prima = True

if n <= 1:
    is_prima = False
else:
    #Memeriksa pembagi dari 2 hingga akar dari n (lebih efisien)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prima = False
            break

#Menampilkan hasil
if is_prima:
    print("Bilangan Prima")
else:
    print("Bukan Bilangan Prima")
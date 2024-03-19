def tampilkan_deret(tinggi, lebar):
    angka = 1
    for i in range(tinggi):
        for j in range(lebar):
            print(angka, end=' ')
            angka += 1
        print()

tinggi = int(input("Masukkan tinggi deret: "))
lebar = int(input("Masukkan lebar deret: "))

tampilkan_deret(tinggi, lebar)
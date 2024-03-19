def bilangan_prima(angka):
    if angka < 2:
        return False
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return False
    return True

def cari_angka_prima_terdekat(n):
    if n < 2:
        return None
    prima = n - 1
    while prima >= 2:
        if bilangan_prima(prima):
            return prima
        prima -= 1
    return None

n = int(input("Masukkan bilangan: "))
prima_deket = cari_angka_prima_terdekat(n)
if prima_deket:
    print(f"Prima terdekat < {n} adalah {prima_deket}")
else:
    print(f"Tidak ada bilangan prima terdekat < {n}")
def print_pattern(n):
    for i in range(n, 0, -1):
        result = 1
        for j in range(i, 0, -1):
            result *= j
        print(result, end=' ')
        for k in range(i, 0, -1):
            print(k, end=' ')
        print()

n = int(input("Masukkan nilai n: "))
print_pattern(n)
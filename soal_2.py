total = 0
for i in range(3):
    angka = int(input(f"Masukkan setoran ke-{i+1}: "))
    if angka <= 0:
        print("Input tidak valid")
        break
    total += angka
else:
    if total < 300000:
        print("rendah")
    elif total < 600000:
        print("sedang")
    else:
        print("tinggi")
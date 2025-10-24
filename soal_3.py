def hitung_ongkir(berat_kg, kota, asuransi=False):
    """
    Function untuk menghitung berat barang ke kota tujuan
    """
    
    tarif_dasar = {
        "Jakarta": 10000,
        "Surabaya": 15000
    }
    
    total = tarif_dasar[kota] + 2000 * berat_kg
    if asuransi:
        total += 3000
        
    return total
    
hasil = hitung_ongkir(10, "Jakarta", True)
print(hasil)

hasil = hitung_ongkir(10, "Surabaya")
print(hasil)
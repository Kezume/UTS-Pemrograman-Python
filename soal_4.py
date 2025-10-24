def jadwal_hari(hari):
    """
    Pencarian harus mengecek satu persatu
    """
    jadwal = [
        {"hari": "Senin", "mata_kuliah": "Algoritma dan Pemrograman"}, # ini dictionary
        {"hari": "Selasa", "mata_kuliah": "Struktur data"},
        {"hari": "Rabu", "mata_kuliah": "Basis Data"},
        {"hari": "Kamis", "mata_kuliah": "Jaringan Komputer"},
        {"hari": "Jumat", "mata_kuliah": "Pemrograman Web"},
    ] # pakai list
    
    for item in jadwal:
        if item["hari"].lower() == hari.lower():
            return f"Jadwal hari {hari}: {item['mata_kuliah']}"
        
    return f"Tidak ada jadwal pada hari {hari}"
    
print(jadwal_hari("Rabu"))
print(jadwal_hari("Minggu"))
import csv
import json
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO, 
    # untuk memformat waktu pada log
    format='%(asctime)s - %(levelname)s - %(message)s'
    
)

def rekap_kehadiran_uts():
    try:
        logging.info("Proses rekap kehadiran dimulai.")

        data_folder = Path("data")
        data_folder.mkdir(exist_ok=True)
        
        csv_path = data_folder / "presensi.csv"
        json_path = data_folder / "ringkasan.json"

        data_presensi = [
            ['A01', 'Agus Citraland', 1],
            ['A02', 'Windah Habbatusaudah', 1],
            ['A03', 'Andi Wijaya', 0],
            ['A04', 'Eko Kurniawan', 1],
        ]
        
        with csv_path.open('w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['nim', 'nama', 'hadir_uts'])
            writer.writerows(data_presensi)

        hadir = 0
        with csv_path.open('r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)

            mahasiswa = list(reader)
            total = len(mahasiswa)
            hadir = sum(1 for baris in mahasiswa if baris[2] == '1')

        persentase = (hadir / total * 100) if total > 0 else 0

        ringkasan = {
            "total_mahasiswa": total,
            "jumlah_hadir": hadir,
            "persentase_kehadiran": f"{persentase:.2f}%"
        }
        with json_path.open('w', encoding='utf-8') as f:
            json.dump(ringkasan, f, indent=4)
        
        logging.info(f"Proses rekap berhasil. Ringkasan disimpan di '{json_path}'.")
        print("Proses rekap kehadiran berhasil diselesaikan.")
    except Exception as e:
        logging.error(f"Terjadi kegagalan: {e}")
        print(f"Proses gagal. {e}")

if __name__ == "__main__":
    rekap_kehadiran_uts()
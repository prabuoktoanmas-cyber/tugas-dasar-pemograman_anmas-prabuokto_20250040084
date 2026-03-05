# WEEK 2 ASSIGNMENT - Python
# Nama: Anmas Prabuokto
# NIM: 20250040084

"""
Program kalkulator keuangan sederhana dengan 5 fitur:
1. Split Bill Nongkrong - Membagi tagihan dengan pajak
2. Konversi Waktu Freelance - Menghitung bayaran berdasarkan waktu kerja
3. Estimasi BBM - Menghitung biaya bahan bakar perjalanan
4. Gaji Bersih Karyawan - Menghitung gaji setelah potongan
5. Penyusutan Nilai Barang - Menghitung penyusutan garis lurus
"""

import math

# Konstanta
PAJAK_SPLIT_BILL = 0.10
KONSUMSI_BBM = 40  # km per liter
HARGA_BBM_PER_LITER = 13000
BPJS_RATE = 0.02
PAJAK_PENGHASILAN = 0.05


def get_valid_float(prompt: str, min_value: float = 0) -> float:
    """
    Mendapatkan input float yang valid dari user dengan validasi.

    Args:
        prompt: Pesan untuk meminta input
        min_value: Nilai minimum yang diperbolehkan

    Returns:
        float: Nilai yang valid
    """
    while True:
        try:
            value = float(input(prompt))
            if value < min_value:
                print(f"Nilai harus lebih besar atau sama dengan {min_value}")
                continue
            return value
        except ValueError:
            print("Masukkan angka yang valid!")


def get_valid_int(prompt: str, min_value: int = 1) -> int:
    """
    Mendapatkan input integer yang valid dari user dengan validasi.

    Args:
        prompt: Pesan untuk meminta input
        min_value: Nilai minimum yang diperbolehkan

    Returns:
        int: Nilai yang valid
    """
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                print(f"Nilai harus lebih besar atau sama dengan {min_value}")
                continue
            return value
        except ValueError:
            print("Masukkan angka bulat yang valid!")


def split_bill():
    """
    Menghitung pembagian tagihan nongkrong dengan pajak 10%.
    Menampilkan total setelah pajak dan bayar per orang.
    """
    print("\n" + "="*50)
    print("           SPLIT BILL NONGKRONG")
    print("="*50)

    total_tagihan = get_valid_float("Masukkan total tagihan (Rp): ")
    jumlah_orang = get_valid_int("Masukkan jumlah orang: ")

    total_setelah_pajak = total_tagihan + (total_tagihan * PAJAK_SPLIT_BILL)
    per_orang = total_setelah_pajak / jumlah_orang

    print("\nHasil Perhitungan:")
    print("-" * 30)
    print(f"Total tagihan awal    : Rp {total_tagihan:,.0f}")
    print(f"Pajak (10%)           : Rp {total_tagihan * PAJAK_SPLIT_BILL:,.0f}")
    print(f"Total setelah pajak   : Rp {total_setelah_pajak:,.0f}")
    print(f"Jumlah orang          : {jumlah_orang}")
    print(f"Bayar per orang       : Rp {per_orang:,.0f}")


def freelance():
    """
    Menghitung bayaran freelance berdasarkan waktu kerja.
    Mengkonversi jam dan menit ke format desimal.
    """
    print("\n" + "="*50)
    print("        KONVERSI WAKTU KERJA FREELANCE")
    print("="*50)

    jam = get_valid_int("Masukkan jam kerja: ", 0)
    menit = get_valid_int("Masukkan menit kerja (0-59): ", 0)

    if menit >= 60:
        print("Menit tidak boleh lebih dari 59!")
        return

    upah_per_jam = get_valid_float("Masukkan upah per jam (Rp): ")

    total_jam = jam + (menit / 60)
    total_bayar = total_jam * upah_per_jam

    print("\nHasil Perhitungan:")
    print("-" * 30)
    print(f"Waktu kerja          : {jam} jam {menit} menit")
    print(f"Total jam (desimal)  : {total_jam:.2f} jam")
    print(f"Upah per jam         : Rp {upah_per_jam:,.0f}")
    print(f"Total bayaran        : Rp {total_bayar:,.0f}")


def estimasi_bbm():
    """
    Mengestimasi biaya bahan bakar untuk perjalanan.
    Berdasarkan konsumsi 1 liter per 40 km.
    """
    print("\n" + "="*50)
    print("           ESTIMASI BBM PERJALANAN")
    print("="*50)

    jarak = get_valid_float("Masukkan jarak perjalanan (km): ")

    liter_dibutuhkan = jarak / KONSUMSI_BBM
    total_biaya = liter_dibutuhkan * HARGA_BBM_PER_LITER

    print("\nHasil Perhitungan:")
    print("-" * 30)
    print(f"Jarak perjalanan     : {jarak:.1f} km")
    print(f"Konsumsi BBM         : 1 liter per {KONSUMSI_BBM} km")
    print(f"Harga BBM per liter  : Rp {HARGA_BBM_PER_LITER:,.0f}")
    print(f"Liter dibutuhkan     : {liter_dibutuhkan:.2f} liter")
    print(f"Total biaya BBM      : Rp {total_biaya:,.0f}")


def gaji_bersih():
    """
    Menghitung gaji bersih karyawan setelah potongan BPJS dan pajak.
    """
    print("\n" + "="*50)
    print("            GAJI BERSIH KARYAWAN")
    print("="*50)

    gaji_pokok = get_valid_float("Masukkan gaji pokok (Rp): ")
    tunjangan = get_valid_float("Masukkan tunjangan (Rp): ", 0)

    potongan_bpjs = gaji_pokok * BPJS_RATE
    potongan_pajak = gaji_pokok * PAJAK_PENGHASILAN
    total_potongan = potongan_bpjs + potongan_pajak
    gaji_total = gaji_pokok + tunjangan - total_potongan

    print("\nHasil Perhitungan:")
    print("-" * 30)
    print(f"Gaji pokok           : Rp {gaji_pokok:,.0f}")
    print(f"Tunjangan            : Rp {tunjangan:,.0f}")
    print(f"Potongan BPJS (2%)    : Rp {potongan_bpjs:,.0f}")
    print(f"Potongan Pajak (5%)   : Rp {potongan_pajak:,.0f}")
    print(f"Total potongan       : Rp {total_potongan:,.0f}")
    print(f"Gaji bersih          : Rp {gaji_total:,.0f}")


def penyusutan():
    """
    Menghitung penyusutan nilai barang menggunakan metode garis lurus.
    Menampilkan penyusutan per tahun dan nilai setelah 2 tahun.
    """
    print("\n" + "="*50)
    print("       PENYUSUTAN NILAI BARANG (GARIS LURUS)")
    print("="*50)

    harga_awal = get_valid_float("Masukkan harga awal (Rp): ")
    nilai_sisa = get_valid_float("Masukkan nilai sisa (Rp): ", 0)
    umur = get_valid_int("Masukkan umur ekonomis (tahun): ")

    if nilai_sisa >= harga_awal:
        print("Nilai sisa tidak boleh lebih besar atau sama dengan harga awal!")
        return

    penyusutan_per_tahun = (harga_awal - nilai_sisa) / umur
    nilai_setelah_2_tahun = harga_awal - (2 * penyusutan_per_tahun)

    print("\nHasil Perhitungan:")
    print("-" * 30)
    print(f"Harga awal           : Rp {harga_awal:,.0f}")
    print(f"Nilai sisa           : Rp {nilai_sisa:,.0f}")
    print(f"Umur ekonomis        : {umur} tahun")
    print(f"Penyusutan per tahun : Rp {penyusutan_per_tahun:,.0f}")
    print(f"Nilai setelah 2 tahun: Rp {nilai_setelah_2_tahun:,.0f}")


def main():
    """
    Fungsi utama program yang menampilkan menu dan menangani pilihan user.
    """
    print("="*60)
    print("         PROGRAM KALKULATOR KEUANGAN SEDERHANA")
    print("              WEEK 2 ASSIGNMENT - PYTHON")
    print("="*60)
    print("Nama: Anmas Prabuokto")
    print("NIM : 20250040084")
    print("="*60)

    while True:
        print("\n" + "="*50)
        print("                    MENU UTAMA")
        print("="*50)
        print("1. Split Bill Nongkrong")
        print("2. Konversi Waktu Kerja Freelance")
        print("3. Estimasi BBM Perjalanan")
        print("4. Gaji Bersih Karyawan")
        print("5. Penyusutan Nilai Barang")
        print("0. Keluar Program")
        print("="*50)

        pilihan = input("Pilih menu (0-5): ").strip()

        if pilihan == "1":
            split_bill()
        elif pilihan == "2":
            freelance()
        elif pilihan == "3":
            estimasi_bbm()
        elif pilihan == "4":
            gaji_bersih()
        elif pilihan == "5":
            penyusutan()
        elif pilihan == "0":
            print("\n" + "="*50)
            print("         TERIMA KASIH TELAH MENGGUNAKAN PROGRAM")
            print("="*50)
            break
        else:
            print("❌ Pilihan tidak valid! Masukkan angka 0-5.")

        input("\nTekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    main()
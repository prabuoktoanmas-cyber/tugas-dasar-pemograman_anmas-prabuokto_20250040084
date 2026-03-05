# 🧮 Tugas Dasar Pemrograman - Week 2 Assignment

## 📋 Informasi Mahasiswa
- **Nama**: Anmas Prabuokto
- **NIM**: 20250040084
- **Mata Kuliah**: Dasar Pemograman
- **Week**: 2
- **Bahasa Pemograman**: Python 3.x

---

## 🎯 Deskripsi Program

**Tugas Dasar Pemrograman** yang dibuat dengan bahasa Python untuk memenuhi tugas Week 2 mata kuliah Dasar Pemograman. Program ini menyediakan **5 fitur utama** untuk menghitung berbagai aspek keuangan sehari-hari dengan interface yang user-friendly dan validasi input yang ketat.

---

## ✨ Fitur Program

### 1. 💰 Split Bill Nongkrong
Menghitung pembagian tagihan nongkrong dengan pajak restoran 10%.

**Input:**
- Total tagihan (Rp)
- Jumlah orang yang ikut

**Output:**
- Total tagihan awal
- Pajak 10%
- Total setelah pajak
- Bayar per orang

### 2. ⏰ Konversi Waktu Kerja Freelance
Menghitung bayaran freelance berdasarkan waktu kerja yang fleksibel.

**Input:**
- Jam kerja
- Menit kerja (0-59)
- Upah per jam (Rp)

**Output:**
- Total waktu kerja (jam:menit)
- Total jam dalam format desimal
- Total bayaran

### 3. 🚗 Estimasi BBM Perjalanan
Mengestimasi biaya bahan bakar untuk perjalanan berdasarkan konsumsi kendaraan.

**Input:**
- Jarak perjalanan (km)

**Output:**
- Jarak perjalanan
- Konsumsi BBM (1 liter per 40 km)
- Harga BBM per liter (Rp 13,000)
- Liter BBM dibutuhkan
- Total biaya BBM

### 4. 💼 Gaji Bersih Karyawan
Menghitung gaji bersih karyawan setelah potongan BPJS dan pajak penghasilan.

**Input:**
- Gaji pokok (Rp)
- Tunjangan (Rp)

**Output:**
- Gaji pokok
- Tunjangan
- Potongan BPJS (2%)
- Potongan Pajak (5%)
- Total potongan
- Gaji bersih diterima

### 5. 📉 Penyusutan Nilai Barang (Garis Lurus)
Menghitung penyusutan nilai barang menggunakan metode garis lurus (straight-line depreciation).

**Input:**
- Harga awal barang (Rp)
- Nilai sisa/residual (Rp)
- Umur ekonomis (tahun)

**Output:**
- Harga awal
- Nilai sisa
- Umur ekonomis
- Penyusutan per tahun
- Nilai setelah 2 tahun

---

## 🚀 Cara Menjalankan Program

### 📋 Persyaratan Sistem
- **Python**: Versi 3.6 atau lebih baru
- **OS**: Windows, macOS, atau Linux
- **Terminal/Command Prompt**: Untuk menjalankan program

### 📝 Langkah-langkah Instalasi dan Menjalankan:

1. **Clone atau Download** repository ini
2. **Buka Terminal/Command Prompt**
3. **Navigasi ke folder project**:
   ```bash
   cd tugas-dasar-pemograman_anmas-prabuokto_20250040084
   ```
4. **Jalankan program**:
   ```bash
   python week2_assigment.py
   ```
5. **Pilih menu** yang diinginkan (1-5) atau tekan 0 untuk keluar

---

## 📁 Struktur Kode

```
week2_assigment.py
├── 📄 Header & Dokumentasi
│   ├── Informasi mahasiswa
│   └── Deskripsi program
├── 🔧 Konstanta Global
│   ├── PAJAK_SPLIT_BILL = 0.10
│   ├── KONSUMSI_BBM = 40
│   ├── HARGA_BBM_PER_LITER = 13000
│   ├── BPJS_RATE = 0.02
│   └── PAJAK_PENGHASILAN = 0.05
├── 🛠️ Fungsi Utilitas
│   ├── get_valid_float() - Validasi input float
│   └── get_valid_int() - Validasi input integer
├── 🎯 Fungsi Utama Program
│   ├── split_bill() - Split bill nongkrong
│   ├── freelance() - Konversi waktu freelance
│   ├── estimasi_bbm() - Estimasi BBM
│   ├── gaji_bersih() - Hitung gaji bersih
│   └── penyusutan() - Hitung penyusutan
└── 🎮 main() - Fungsi utama & menu program
```

---

## 🎨 Fitur Tambahan & Keunggulan

### ✅ **Error Handling yang Kuat**
- Validasi input yang ketat
- Pesan error yang informatif
- Mencegah crash program
- Boundary checking untuk semua input

### 🎯 **User Experience yang Excellent**
- Interface menu yang jelas dan menarik
- Output terformat dengan mata uang Rupiah
- Navigasi yang mudah dengan input sederhana
- Pesan bantuan yang informatif

### 🔧 **Kualitas Kode**
- **Modular**: Kode terstruktur dengan fungsi-fungsi terpisah
- **Readable**: Komentar dan docstring yang lengkap
- **Maintainable**: Konstanta untuk nilai tetap
- **Type Hints**: Petunjuk tipe data untuk parameter

### 📊 **Formatted Output**
- Angka dalam format Rupiah (Rp 100,000)
- Decimal formatting yang konsisten
- Layout yang rapi dan mudah dibaca
- Breakdown perhitungan yang detail

---

## 📸 Contoh Penggunaan

### Menu Utama
```
============================================================
         TUGAS DASAR PEMROGRAMAN
              WEEK 2 ASSIGNMENT - PYTHON
============================================================
Nama: Anmas Prabuokto
NIM : 20250040084
============================================================

==================================================
                    MENU UTAMA
==================================================
1. Split Bill Nongkrong
2. Konversi Waktu Kerja Freelance
3. Estimasi BBM Perjalanan
4. Gaji Bersih Karyawan
5. Penyusutan Nilai Barang
0. Keluar Program
==================================================
Pilih menu (0-5):
```

### Contoh Split Bill
```
==================================================
           SPLIT BILL NONGKRONG
==================================================
Masukkan total tagihan (Rp): 100000
Masukkan jumlah orang: 4

Hasil Perhitungan:
------------------------------
Total tagihan awal    : Rp 100,000
Pajak (10%)           : Rp 10,000
Total setelah pajak   : Rp 110,000
Jumlah orang          : 4
Bayar per orang       : Rp 27,500
```

### Contoh Gaji Bersih
```
==================================================
            GAJI BERSIH KARYAWAN
==================================================
Masukkan gaji pokok (Rp): 5000000
Masukkan tunjangan (Rp): 1000000

Hasil Perhitungan:
------------------------------
Gaji pokok           : Rp 5,000,000
Tunjangan            : Rp 1,000,000
Potongan BPJS (2%)    : Rp 100,000
Potongan Pajak (5%)   : Rp 250,000
Total potongan       : Rp 350,000
Gaji bersih          : Rp 5,650,000
```

---

## 🧪 Testing & Validasi

### ✅ **Test Cases yang Telah Dilakukan:**
- **Split Bill**: Input valid dan invalid, perhitungan akurat
- **Freelance**: Konversi waktu jam:menit ke desimal
- **BBM**: Perhitungan konsumsi dan biaya
- **Gaji**: Potongan BPJS dan pajak penghasilan
- **Penyusutan**: Metode garis lurus depreciation

### ✅ **Error Handling Test:**
- Input non-numeric → Error message
- Nilai negatif → Validation error
- Input kosong → Error message
- Boundary values → Proper handling

---

## 📚 Teknologi & Konsep yang Digunakan

### 💻 **Bahasa Pemograman**
- **Python 3.x**: Modern, readable, dan powerful

### 🏗️ **Paradigm Programming**
- **Procedural Programming**: Struktur program yang jelas
- **Modular Programming**: Fungsi-fungsi terpisah dan reusable

### 🔧 **Konsep Pemograman**
- **Input Validation**: Validasi input user
- **Error Handling**: Try-except blocks
- **Constants**: Nilai tetap untuk maintainability
- **Functions**: Modular code structure
- **Looping**: While loops untuk menu
- **Conditional**: If-elif-else untuk menu selection

### 📦 **Library yang Digunakan**
- **Built-in Python**: math, sys (implisit)
- **No external dependencies**: Standalone program

---

## 🎓 Pembelajaran yang Diperoleh

Dalam pembuatan program ini, penulis telah mempelajari dan mengimplementasikan:

1. **Input/Output Handling** - Validasi dan formatting input user
2. **Error Handling** - Exception handling dan user-friendly error messages
3. **Modular Programming** - Struktur kode yang terorganisir
4. **Constants & Variables** - Penggunaan konstanta untuk maintainability
5. **String Formatting** - f-strings dan format mata uang
6. **Control Flow** - Loops dan conditional statements
7. **Documentation** - Docstrings dan komentar yang baik
8. **User Experience** - Interface yang intuitif dan informatif

---

## 📞 Kontak & Support

**Mahasiswa:**
- Nama: Anmas Prabuokto
- NIM: 20250040084
- Email: [Email mahasiswa]
- GitHub: [GitHub username]

**Dosen Pengampu:**
- Mata Kuliah: Dasar Pemograman
- Semester: [Semester]
- Tahun Akademik: [Tahun Akademik]

---

## 📋 Catatan Penting

- Program ini dibuat sebagai tugas mata kuliah Dasar Pemograman
- Kode dapat dikembangkan lebih lanjut dengan fitur tambahan
- Pastikan Python 3.6+ terinstall sebelum menjalankan program
- Program telah ditest pada Windows, macOS, dan Linux

---

**Terima kasih telah menggunakan Tugas Dasar Pemrograman! 🎉**

---

*Created with ❤️ by Anmas Prabuokto - 20250040084*
Total setelah pajak   : Rp 110,000
Jumlah orang          : 4
Bayar per orang       : Rp 27,500
```

## Teknologi yang Digunakan
- **Bahasa Pemograman**: Python 3
- **Library**: Built-in Python (math, sys)
- **Paradigm**: Procedural Programming

## Pembelajaran yang Diperoleh
- Input validation dan error handling
- Modular programming dengan functions
- Constants dan best practices
- User interface design
- Formatted output dengan f-strings
- Type hints (optional)

---

**Catatan**: Program ini dibuat sebagai tugas mata kuliah Dasar Pemograman dan dapat dikembangkan lebih lanjut dengan fitur tambahan.
# Tugas Dasar Pemrograman - Week 2 Assignment

## Informasi Mahasiswa
Nama : Anmas Prabuokto  
NIM  : 20250040084  
Mata Kuliah : Dasar Pemograman  

---

## Deskripsi Program
Program ini dibuat untuk memenuhi tugas Week 2 mata kuliah Dasar Pemograman. Program berisi lima pilihan perhitungan keuangan sederhana.

---

## Menu Program
1. Split Bill Nongkrong  
2. Konversi Waktu Kerja Freelance  
3. Estimasi BBM Perjalanan  
4. Gaji Bersih Karyawan  
5. Penyusutan Nilai Barang  
0. Keluar

Penjelasan masing-masing menu ada di dalam program.

---

## Cara Menjalankan

1. Pastikan Python 3 sudah terpasang.  
2. Buka terminal dan masuk ke folder project.  
3. Jalankan:
   ```bash
   python week2_assigment.py
   ```
4. Masukkan angka menu sesuai yang diinginkan.

---

## Contoh Penggunaan

Contoh input untuk menu split bill:

```
1
100000
4
```

Maka outputnya:

```
Total tagihan awal    : Rp 100000
Pajak (10%)           : Rp 10000
Total setelah pajak   : Rp 110000
Jumlah orang          : 4
Bayar per orang       : Rp 27500
```

---

## Struktur File

`week2_assigment.py` berisi semua kode. Silakan buka file tersebut untuk melihat fungsi-fungsinya.

---

_program ini dibuat sendiri oleh mahasiswa untuk tugas kuliah._

---

## Fitur Tambahan

### Error Handling
- Validasi input yang ketat
- Pesan error yang informatif
- Mencegah crash program
- Boundary checking untuk semua input

### User Interface
- Interface menu yang jelas dan menarik
- Output terformat dengan mata uang Rupiah
- Navigasi yang mudah dengan input sederhana
- Pesan bantuan yang informatif

### Kualitas Kode
- **Modular**: Kode terstruktur dengan fungsi-fungsi terpisah
- **Readable**: Komentar dan docstring yang lengkap
- **Maintainable**: Konstanta untuk nilai tetap
- **Type Hints**: Petunjuk tipe data untuk parameter

### Format Output
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
- Email: [prabuoktoanmas@gmail.com]
- GitHub: [prabuoktoanmas-cyber]

**Dosen Pengampu:**
- Mata Kuliah: Dasar Pemograman
- Semester: [2]
- Tahun Akademik: [2026]

---

## 📋 Catatan Penting

- Program ini dibuat sebagai tugas mata kuliah Dasar Pemograman
- Kode dapat dikembangkan lebih lanjut dengan fitur tambahan
- Pastikan Python 3.6+ terinstall sebelum menjalankan program
- Program telah ditest pada Windows, macOS, dan Linux

---


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
# 🐍 Praktikum OOP Python – Dunia Binatang

## 🎯 Tujuan
Tugas ini bertujuan untuk mengasah pemahaman kalian terhadap konsep-konsep utama Object-Oriented Programming (OOP), khususnya:
- Inheritance
- Polymorphism
- Abstract Class
- Interface (via Abstract Base Class)

---

## 📝 Deskripsi Tugas

Buatlah program Python yang mensimulasikan dunia binatang menggunakan konsep OOP. Program kalian harus memenuhi kriteria berikut:

### 1. Inheritance
- Buat **class induk** bernama `Hewan` dengan atribut:
  - `nama`
  - `jenis` (contoh: herbivora, karnivora, omnivora)
  - `umur`
- Buat **minimal 2 subclass** dari `Hewan`, misalnya: `Kucing`, `Elang`, `Gajah`, dsb.

### 2. Polymorphism
- Buat method `bersuara()` yang akan di-*override* oleh setiap subclass dengan suara khas masing-masing hewan.

### 3. Abstract Class
- Jadikan `Hewan` sebagai **abstract class** menggunakan modul `abc`.
- Tambahkan method `makan()` sebagai abstract method yang harus diimplementasikan di setiap subclass.

### 4. Interface (via Abstract Class)
- Buat abstract class `Bergerak` yang memiliki method `bergerak()`.
- Subclass `Hewan` bisa meng-*implement* class ini dan memberikan perilaku unik:
  - Contoh: Elang → "Terbang tinggi", Gajah → "Berjalan pelan"

### 5. Tampilan Program
- Buat beberapa objek dari subclass dan tampilkan seluruh informasi mereka:
  - Nama, jenis, umur, suara, cara makan, dan cara bergerak.

## 📦 Format Pengumpulan
- File Python: `NIM_NAMA_W7.py`
- Push ke GitHub dan kirimkan link repository

---

## 📌 Catatan
- Boleh berdiskusi, namun **hasil akhir harus orisinal**.
- Gunakan komentar di dalam kode jika perlu menjelaskan logika.

---

Selamat mengerjakan dan semangat belajar! 🐾

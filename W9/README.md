# ✅ Praktikum OOP Python – Unit Testing

Halo semuanya! 👋  
Di praktikum kali ini, kita akan membahas topik penting dalam pengembangan perangkat lunak modern, yaitu **Unit Testing**. Tujuan dari unit testing adalah memastikan setiap **bagian kecil (unit)** dari program kita bekerja dengan benar, terutama **fungsi dan metode dalam class**.

---

## 🧪 Apa Itu Unit Testing?

Unit Testing adalah proses **menguji bagian terkecil dari kode**—biasanya fungsi atau metode—secara terpisah, untuk memastikan bahwa hasilnya sesuai harapan.

Python menyediakan modul built-in bernama `unittest` untuk membantu membuat dan menjalankan pengujian otomatis.

---

## 🔧 Modul `unittest` di Python

Modul `unittest` memungkinkan kita untuk:

- Membuat class khusus yang menguji class atau fungsi kita
- Menuliskan **tes otomatis**
- Menjalankan semua tes dengan sekali jalan (langsung dari terminal)

---

## 🧱 Contoh Program Unit Testing

```python
import unittest

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Dipanggil sebelum setiap tes dijalankan
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

if __name__ == '__main__':
    unittest.main()

```

---

## 🔍 Penjelasan Program

- `Calculator`: class sederhana dengan dua metode (add dan subtract).
- `TestCalculato`r: class turunan dari unittest.TestCase yang digunakan untuk mengelompokkan tes.
- `setUp()`: dijalankan sebelum setiap metode tes, untuk menyiapkan objek yang akan diuji.
- `test_add()` dan `test_subtract()`:
  - Menggunakan `self.assertEqual()` untuk membandingkan hasil aktual dan hasil yang diharapkan.
- `unittest.main()`: menjalankan semua tes yang ada saat file dijalankan.

---

## 🧠 Kenapa Unit Test Itu Penting?

- Membantu menemukan bug lebih awal
- Menghindari error yang tidak terduga di masa depan
- Membuat proses refactoring kode lebih aman
- Membangun kebiasaan coding yang profesional

---

## 🧪 Cara Menjalankan Tes

```bash
python test_ticket_system.py
```

Jika berhasil, output-nya akan seperti ini:

```bash
....
-----------------------------------------------------------
Ran 4 tests in 0.002s
```

---

## ✍️ Tugas Praktikum

Silahkan cek ke repository GitHub `PraktikumOOPA2/W9`

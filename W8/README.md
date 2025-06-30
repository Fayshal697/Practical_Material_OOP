# 🐍 Praktikum OOP Python – Exception Handling

Halo semuanya! 👋  
Di praktikum kali ini, kita akan belajar tentang **Exception Handling** alias **penanganan error saat program dijalankan**. Ini penting banget biar program kita gak langsung "meledak" pas ada kesalahan, tapi tetap bisa berjalan dengan elegan.

---

## 🧠 Apa Itu Exception?

Exception adalah **kesalahan yang terjadi saat program berjalan (runtime error)**. Contoh yang sering ditemui:

- Bagi angka dengan nol (`ZeroDivisionError`)
- Input bukan angka (`ValueError`)
- Akses atribut yang belum ada (`AttributeError`)
- File tidak ditemukan (`FileNotFoundError`)

---

## 🔧 Kenapa Harus Pakai Exception Handling?

Tanpa exception handling, program akan langsung **berhenti dan error**.  
Dengan exception handling, kita bisa:

- Menangani error dengan cara yang lebih aman
- Memberikan pesan yang ramah ke pengguna
- Menjaga program tetap berjalan

---

## 🛠️ Struktur Dasar Try-Except

```python
try:
    # kode yang berpotensi error
except TipeError:
    # apa yang dilakukan kalau error terjadi
else:
    # (opsional) dijalankan jika tidak ada error
finally:
    # (opsional) dijalankan selalu, error atau tidak

```

## 📌 Contoh-Contoh

### 1. Bagi Dengan Nol (0)

```python
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol.")
```

### 2. Atribut Yang Tidak Ada

```python
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

mhs = Mahasiswa("Ayu", "20240101")

try:
    print(mhs.jurusan)
except AttributeError:
    print("Atribut 'jurusan' belum dibuat.")
```

### 3. Input Dari User

```python
try:
    angka = int(input("Masukkan angka: "))
    print(10 / angka)
except ValueError:
    print("Input harus berupa angka.")
except ZeroDivisionError:
    print("Tidak bisa bagi nol.")
```

## 🎯 Tujuan Praktikum

- Mahasiswa memahami konsep dasar exception handling
- Mahasiswa dapat mengimplementasikan try-except di program Python
- Mahasiswa terbiasa membaca dan memahami pesan error
- Mahasiswa mengetahui pentingnya menangani error saat OOP

## ✍️ Tugas Praktikum

Untuk Tugas Silahkan di cek dalam repository Github `PraktikumOOPA2`

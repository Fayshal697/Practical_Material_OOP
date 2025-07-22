# Refactoring dalam OOP (Object-Oriented Programming)

## 📌 Materi Singkat

Refactoring adalah proses **perbaikan struktur internal kode** tanpa mengubah **perilaku eksternal** dari kode tersebut. Tujuan utamanya adalah membuat kode menjadi lebih mudah dibaca, dipelihara, dan diperluas.

Beberapa teknik refactoring dalam OOP:

- **Extract Method**: Memisahkan bagian kode menjadi metode baru untuk meningkatkan keterbacaan dan menghindari duplikasi.
- **Rename Method**: Mengubah nama metode agar lebih menggambarkan fungsinya.
- **Move Method**: Memindahkan metode ke kelas yang lebih relevan jika fungsinya lebih berkaitan dengan kelas lain.

---

## 💻 Contoh Program Sebelum dan Sesudah Refactoring

### 🔴 Sebelum Refactoring

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Jumlah deposit tidak valid")
        else:
            self.balance += amount
            print(f"Deposit {amount} berhasil")

    def withdraw(self, amount):
        if amount <= 0:
            print("Jumlah penarikan tidak valid")
        elif amount > self.balance:
            print("Saldo tidak cukup")
        else:
            self.balance -= amount
            print(f"Penarikan {amount} berhasil")
```

### ✅ Setelah Refactoring (Extract Method)

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if not self.valid_amount(amount):
            print("Jumlah deposit tidak valid")
        else:
            self.balance += amount
            print(f"Deposit {amount} berhasil")

    def withdraw(self, amount):
        if not self.valid_amount(amount):
            print("Jumlah penarikan tidak valid")
        elif amount > self.balance:
            print("Saldo tidak cukup")
        else:
            self.balance -= amount
            print(f"Penarikan {amount} berhasil")

    def valid_amount(self, amount):
        return amount > 0
```

---

## 📖 Penjelasan Program

Pada contoh di atas, dilakukan Extract Method dengan menambahkan fungsi `valid_amount()` untuk memvalidasi jumlah transaksi. Ini memberikan manfaat:

- Menghindari **duplikasi kode** pada `deposit()` dan `withdraw()`
- Meningkatkan **keterbacaan**
- Memudahkan **perawatan** jika aturan validasi berubah di masa depan

---

## 📚 Catatan

Refactoring adalah bagian penting dalam pengembangan perangkat lunak berorientasi objek yang bersih dan berkelanjutan. Gunakan refactoring secara rutin untuk menjaga kualitas kode.

---

## ✍️ Tugas Praktikum

Silahkan cek ke repository GitHub `PraktikumOOPA2/TugasW10`

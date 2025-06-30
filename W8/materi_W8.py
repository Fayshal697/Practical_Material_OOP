# STRUKTUR PENULISAN DASAR EXCEPTION HANDLING

#try:
    # kode yang mungkin error
#except:
    # apa yang dilakukan kalau error terjadi
#else:
    # OPSIONAL - jika tidak ada error
#finally:
    # OPSIONAL - selalu dijalankan, mau error ataupun tidak




# CONTOH 1: Menangani Pembagian dengan Nol
def bagi(a, b):
    try:
        hasil = a / b
        print(f"Hasil: {hasil}")
    except ZeroDivisionError:
        print("Error: Tidak bisa membagi dengan nol")
    else:
        print("Pembagian berhasil!")
    finally:
        print("Selesai menghitung")

bagi(10, 2)
bagi(60, 10)




# CONTOH 2: Penanganan Atribut yang Kurang (OOP Context)
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

mhs = Mahasiswa("Ali", "20240101")

try:
    print(mhs.jurusan)  # Atribut tidak ada
except AttributeError as e:
    print(f"AttributeError: {e}")

# outputnya menjelaska kesalahan, dan program tidak langsung crash




# CONTOH 3: Menangani Banyak Jenis Error
try:
    angka = int(input("Masukkan angka: "))
    print(10 / angka)
except ValueError:
    print("Input bukan angka!")
except ZeroDivisionError:
    print("Tidak bisa bagi nol!")
except Exception as e:
    print(f"Terjadi error lainnya: {e}")




#TIPS

#1. Ajak teman kamu untuk mencoba men-trigger error sendiri (ex: ketik atribut salah).
#2. Tunjukkan manfaat dari try-except → program tetap jalan walau error.
#3. Jelaskan bahwa bisa juga buat custom exception (level lanjut OOP).
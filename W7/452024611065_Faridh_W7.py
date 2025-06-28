# ### 1. Inheritance
# - Buat **class induk** bernama `Hewan` dengan atribut:
#   - `nama`
#   - `jenis` (contoh: herbivora, karnivora, omnivora)
#   - `umur`
# - Buat **minimal 2 subclass** dari `Hewan`, misalnya: `Kucing`, `Elang`, `Gajah`, dsb.

# ### 3. Abstract Class
# - Jadikan `Hewan` sebagai **abstract class** menggunakan modul `abc`.
# - Tambahkan method `makan()` sebagai abstract method yang harus diimplementasikan di setiap subclass.
#
# ### 4. Interface (via Abstract Class)
# - Buat abstract class `Bergerak` yang memiliki method `bergerak()`.
# - Subclass `Hewan` bisa meng-*implement* class ini dan memberikan perilaku unik:
#   - Contoh: Elang → "Terbang tinggi", Gajah → "Berjalan pelan"


from abc import ABC, abstractmethod


class Bergerak(ABC):
    @abstractmethod
    def bergerak(self):
        pass


class Hewan(ABC):
    def __init__(self, nama, jenis, umur):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur

    def bersuara(self):
        print("Hewan Bersuara")

    @abstractmethod
    def makan(self):
        pass


class Kucing(Hewan, Bergerak):
    def __init__(self, nama, jenis, umur):
        super().__init__(nama, jenis, umur)

        print("Kucing dengan nama", self.nama, "berumur", self.umur, "tahun")

    def bersuara(self):
        print("Kucing Bersuara: Meow")

    def makan(self):
        print("Kucing Makan Ikan")

    def bergerak(self):
        print("Kucing Berjalan Pelan")


class Gajah(Hewan, Bergerak):
    def __init__(self, nama, jenis, umur):
        super().__init__(nama, jenis, umur)

        print("Gajah dengan nama", self.nama, "berumur", self.umur, "tahun")

    def bersuara(self):
        print("Gajah Bersuara")

    def makan(self):
        print("Gajah Makan Daging")

    def bergerak(self):
        print("Gajah Berjalan Pelan")


if __name__ == "__main__":
    kucing = Kucing("Kucing", "Herbivora", 2)
    gajah = Gajah("Gajah", "Karnivora", 10)

    kucing.bersuara()
    gajah.bersuara()

    kucing.makan()
    gajah.makan()

    kucing.bergerak()
    gajah.bergerak()

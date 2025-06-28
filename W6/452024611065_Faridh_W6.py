# ### 1. Inheritance
# - Buat **class induk** bernama `Hewan` dengan atribut:
#   - `nama`
#   - `jenis` (contoh: herbivora, karnivora, omnivora)
#   - `umur`
# - Buat **minimal 2 subclass** dari `Hewan`, misalnya: `Kucing`, `Elang`, `Gajah`, dsb.


class Hewan:
    def __init__(self, nama, jenis, umur):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur

    def bersuara(self):
        print("Hewan Bersuara")


class Kucing(Hewan):
    def __init__(self, nama, jenis, umur):
        super().__init__(nama, jenis, umur)

        print("Kucing dengan nama", self.nama, "berumur", self.umur, "tahun")

    def bersuara(self):
        print("Kucing Bersuara: Meow")


class Gajah(Hewan):
    def __init__(self, nama, jenis, umur):
        super().__init__(nama, jenis, umur)

        print("Gajah dengan nama", self.nama, "berumur", self.umur, "tahun")

    def bersuara(self):
        print("Gajah Bersuara")


if __name__ == "__main__":
    kucing = Kucing("Kucing", "Herbivora", 2)
    gajah = Gajah("Gajah", "Karnivora", 10)

    kucing.bersuara()
    gajah.bersuara()

# STUDI KASUS
# Superclass "Orang" (atributnya: nama, umur, jabatan)
# subclass nya:
# 1. Dosen (atribut tambahan: mata_kuliah)
# 2. Mahasiswa (atribut tambahan: nim, ipk)
# 3. Tenaga Kependidikan (atribut tambahan: gaji)
# 4. Staff (attribut tambahsan: lama_menjabat)
# tes nya wajib pake nama orang
# tes nya berhasil/tidak wajib pakai fungsi


import os


class Orang:
    def __init__(self, nama, umur, jabatan):
        self.nama = nama
        self.umur = umur
        self.jabatan = jabatan


class Dosen(Orang):
    def __init__(self, nama, umur, jabatan, mata_kuliah):
        super().__init__(nama, umur, jabatan)
        self.mata_kuliah = mata_kuliah

    def info(self):
        print(
            f"{'═' * os.get_terminal_size()[0]}\nNama: {self.nama}\nUmur: {self.umur}\nJabatan: {self.jabatan}\nMata Kuliah: {self.mata_kuliah}{'═' * os.get_terminal_size()[0]}"
        )


class Mahasiswa(Orang):
    def __init__(self, nama, umur, jabatan, NIM, IPK):
        super().__init__(nama, umur, jabatan)
        self.NIM = NIM
        self.IPK = IPK

    def info(self):
        print(
            f"{'═' * os.get_terminal_size()[0]}\nNama: {self.nama}\nUmur: {self.umur}\nJabatan: {self.jabatan}\nNIM: {self.NIM}\nIPK: {self.IPK}{'═' * os.get_terminal_size()[0]}"
        )


class TenagaKependidikan(Orang):
    def __init__(self, nama, umur, jabatan, gaji):
        super().__init__(nama, umur, jabatan)
        self.gaji = gaji

    def info(self):
        print(
            f"{'═' * os.get_terminal_size()[0]}\nNama: {self.nama}\nUmur: {self.umur}\nJabatan: {self.jabatan}\nGaji: {self.gaji}{'═' * os.get_terminal_size()[0]}"
        )


class Staff(Orang):
    def __init__(self, nama, umur, jabatan, lama_menjabat):
        super().__init__(nama, umur, jabatan)
        self.lama_menjabat = lama_menjabat

    def info(self):
        print(
            f"{'═' * os.get_terminal_size()[0]}\nNama: {self.nama}\nUmur: {self.umur}\nJabatan: {self.jabatan}\nLama Menjabat: {self.lama_menjabat}{'═' * os.get_terminal_size()[0]}"
        )


if __name__ == "__main__":
    dosen = Dosen("Faridh", 21, "Dosen", "Pemrograman Berorientasi Objek")
    mahasiswa = Mahasiswa("Fulan", 20, "Mahasiswa", "452024611065", 3.9)
    tendik = TenagaKependidikan("Fulan", 20, "Tenaga Kependidikan", 5)
    staff = Staff("Faridh", 21, "Staff", 2)

    dosen.info()
    mahasiswa.info()
    tendik.info()
    staff.info()

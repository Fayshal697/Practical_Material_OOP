# STUDI KASUS
# buat kelas "Mahasiswa" yang dapat menerima: Nama, NIM, IPK (jika tidak ada, maka default nya 0)
# untuk mencetak hasil, dilarang menggunakan "print" dan harus menggunakan metode "memanggil fungsi"

import os


class Mahasiswa:
    def __init__(
        self, Nama: str = "Fulan", NIM: str = "452024611000", IPK: float = 1.0
    ):
        self.Nama = Nama
        self.NIM = NIM
        self.IPK = IPK

    def lihatData(self):
        return f"""{'═' * os.get_terminal_size()[0]}
Nama: {self.Nama}
NIM: {self.NIM}
IPK: {self.IPK}
{"═" * os.get_terminal_size()[0]}"""


if __name__ == "__main__":
    mhs = Mahasiswa("Faridh", "452024611065", 3.91)

    print(mhs.lihatData())

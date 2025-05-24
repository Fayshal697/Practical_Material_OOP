class TokoElektronik:
    def __init__(self, merk, daya):
        self.merk = merk
        self.daya = daya

    def info(self):
        print(f"Perangkat elektronik: {self.merk}, dengan daya: {self.daya} Watt")

class SmartPhone(TokoElektronik):
    def __init__(self, merk, daya, os):
        super().__init__(merk, daya)
        self.os = os

    def info(self):
        super().info()
        print(f"Sistem operasi: {self.os}")

hp = SmartPhone("Samsung", 64, "Android")
hp.info()
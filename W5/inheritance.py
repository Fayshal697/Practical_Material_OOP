class kendaraan:
    def jalan(self):
        print("Kendaraan sedang berjalan...")

class Mobil(kendaraan):
    def klakson(self):
        print("Mobil membunyikan klakson: Tiiinn!!!")

#test
m = Mobil()
m.jalan()
m.klakson()
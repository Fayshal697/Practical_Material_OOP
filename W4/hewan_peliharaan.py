# Superclass
class Hewan:
    def suara(self):
        print("Hewan ini mengeluarkan suara...")

# Subclass Kucing
class Kucing(Hewan):
    def suara(self):
        print("Meong")

# Subclass Anjing
class Anjing(Hewan):
    def suara(self):
        print("Guk guk")

# Contoh penggunaan
kucing1 = Kucing()
anjing1 = Anjing()

kucing1.suara()  # Output: Meong
anjing1.suara()  # Output: Guk guk

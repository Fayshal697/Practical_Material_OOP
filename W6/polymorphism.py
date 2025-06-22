class Hewan:
    def suara(self):
        print("Hewan bersuara")

class Kucing(Hewan):
    def suara(self):
        print("Kucing: Meong")

class Anjing(Hewan):
    def suara(self):
        print("Anjing: Guk guk")

# Main
hewan1 = Kucing()
hewan2 = Anjing()

hewan1.suara()
hewan2.suara()

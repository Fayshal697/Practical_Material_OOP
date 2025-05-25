#superclass
class Kendaraan:
    def __init__(self, merek, roda):
        self.merek = merek
        self.roda = roda

#subclass
class Motor(Kendaraan):
    def __init__(self, merek, roda, horsePower):
        super().__init__(merek, roda)
        self.horsePower = horsePower
        
class Mobil(Kendaraan):
    def __init__(self, merek, roda, transmisi):
        super().__init__(merek, roda)
        self.transmisi = transmisi

motor1 = Motor("Yamaha", 2, 400)

print(f"Hadong punya motor {motor1.merek}, dengan roda {motor1.roda} dengan kapasitas bensinnya {motor1.horsePower}")

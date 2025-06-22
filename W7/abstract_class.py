from abc import ABC, abstractmethod

class BangunDatar(ABC):
    @abstractmethod
    def luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

# Main
p = Persegi(5)
print("Luas:", p.luas())

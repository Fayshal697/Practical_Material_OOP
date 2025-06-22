from abc import ABC, abstractmethod

class Terbang(ABC):
    @abstractmethod
    def terbang(self):
        pass

class Burung(Terbang):
    def terbang(self):
        print("Burung terbang di langit")

class Pesawat(Terbang):
    def terbang(self):
        print("Pesawat lepas landas")

b = Burung()
p = Pesawat()

b.terbang()  # Output: Burung terbang di langit
p.terbang()  # Output: Pesawat lepas landas

#ini adalah tambahan

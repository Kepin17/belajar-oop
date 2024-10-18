from abc import ABC
class hewan(ABC):
  def sifat(self):
    pass

class Singa(hewan):
  def makan(self):
    print("Karnivora")
class Gajah(hewan):
  def makan(self):
    print("Herbivora")
class Kera(hewan):
  def makan(self):
    print("Omnivora")
# Driver code
K = Singa()
K.makan()
H = Gajah()
H.makan()
O = Kera()
O.makan()
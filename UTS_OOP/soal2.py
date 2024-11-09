class Shape: 
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

class RetangleCalc(Shape):
    def __init__(self, panjang, lebar, tinggi):
        super().__init__(panjang, lebar, tinggi)
    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)        

Shape = RetangleCalc(10, 5 , 0)
print(Shape.luas())
print(Shape.keliling())

# Metode yang digunakan :
# 1. Inheritance 
# 2. Encapsulation
# 3. Abstraction 



# Pembuatan Class
class Item:
  def calculate_total_price(self,name, x, y):
   calc = x * y
   return f"harga dari {name} : " + str(calc)

# Pembuatan sub class
item1 = Item()
# Penulisan variabel
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
# Pemanggilan sub class
print(item1.calculate_total_price(item1.name, item1.price, item1.quantity))
# Pembuatan sub class
item2 = Item()
# Penulisan variabel
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
# Pemanggilan sub class
print(item2.calculate_total_price(item2.name, item2.price, item2.quantity))
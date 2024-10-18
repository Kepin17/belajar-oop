class Food:
  name = ""

  def eat(self):
    print("I like eat a fruit")

class Fruit(Food):
  def display(self):
    print(f"My favorite fruit is {self.name}")

objectOne = Fruit()
objectOne.name = "Apple"
objectOne.eat()

objectOne.display()

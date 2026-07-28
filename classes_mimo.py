class Feline:
  def speak(self):
    print("Meow")

class Cat(Feline): # Essa classe é uma herança da Feline
  def lick(self):
    print("Licking paw")

class Lion(Feline): # Essa classe é uma herança da Feline
  def prey(self):
    print("Pounces on prey")


cat = Cat()
cat.speak()                  
lion = Lion()
lion.speak()

# Uma subclasse pode sobrescrever os métodos
# que herda de sua superclasse. Basta definir o método com o 
# mesmo nome na subclasse.

class Feline:
  def speak(self):
    print("Meow")

class Cat(Feline):
  def lick(self):
    print("Licking paw")

class Lion(Feline):
  def prey(self):
    print("Pounces on prey")
  def speak(self):
    print("ROAR!")
    
cat = Cat()
cat.speak()
lion = Lion()
lion.speak()
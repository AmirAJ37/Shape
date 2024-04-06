class Shape:
  def __init__(self, **kwargs):
    for key, value in kwargs.items():
      setattr(self, key, value)
    self.area = 0
    self.perimeter = 0 
  
  def calculate_area(self):
    pass
  
  
  def calculate_perimeter(self):
    pass
  
  
  def info(self, **kwargs):
    info = ""
    for key, value in self.__dict__.items():
      if value > 0 :
        info += f"{key}: {value}\n"
    print(info)


class Rectangle(Shape):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
  
  
  def calculate_area(self):
    self.area = self.length * self.width
  
  
  def calculate_perimeter(self):
    self.perimeter = (self.length + self.width) * 2
  

class Square(Shape):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
  
  
  def calculate_area(self):
    self.area = self.length ** 2
  
  
  def calculate_perimeter(self):
    self.perimeter = self.length * 4
  

class triangle(Shape):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
  
  
  def calculate_area(self):
    self.area = (self.height * self.base) / 2
  
  
  def calculate_perimeter(self):
    self.perimeter = self.base + self.side1 + self.side2

  
class circle(Shape):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
  
  
  def calculate_area(self):
    self.area = self.radius ** 2 * 3.14
  
  
  def calculate_perimeter(self):
    self.perimeter = self.radius * 2 * 3.14
  
def main():
 while True: 
  choice = int(input("wich Shape?\n1.for rectangle\n2.for Square\n3.for triangle\n4.for circle\n5.for exit!"))
  if choice == 1 :
    x = int(input("length: "))
    y = int(input("width: "))
    print(80 * "×")
    r = Rectangle(length=x, width=y)
    r.calculate_perimeter()
    r.calculate_area()
    r.info()
    print(80 * "-")
  elif choice == 2 :
    x = int(input("length: "))
    print(80 * "×")
    s = Square(length=x)
    s.calculate_perimeter()
    s.calculate_area()
    s.info()
    print(80 * "-")
  elif choice == 3 :
    x = int(input("height: "))
    y = int(input("base: "))
    z = int(input("side1: "))
    f = int(input("side2: "))
    print(80 * "×")
    t = triangle(height=x, base=y, side1=z, side2=f)
    t.calculate_perimeter()
    t.calculate_area()
    t.info()
    print(80 * "-")
  elif choice == 4 :
    r = int(input("radius: "))
    print(80 * "×")
    ss = circle(radius=r)
    ss.calculate_perimeter()
    ss.calculate_area()
    ss.info()
    print(80 * "-")
  elif choice == 5 :
    print("Good luck!")
    break

main()
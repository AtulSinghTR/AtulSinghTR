class car:

  car_type = 'sedan'

  def __init__(self,color,mileage):
    self.color = color
    self.mileage = mileage

  def change(self):
    global car_type
    self.car_type = 'sport'
    return 'car_type has been changed to '+self.car_type

  def dummy(self):
    return f'The {self.color} {self.car_type} has {self.mileage:,} miles.'


blue = car('blue', 20_000)
print(blue.dummy())
print(blue.change())
print(blue.dummy())

print("")
green = car('green', 40_000)
print(green.dummy())


print("")
yellow = car('yellow', 40_000)
print(yellow.dummy())
print(yellow.change())
print(yellow.dummy())





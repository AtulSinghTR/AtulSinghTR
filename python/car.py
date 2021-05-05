class car:
  def __init__(self,color,mileage):
    self.color = color
    self.mileage = mileage
    self.out = f'The {self.color} has {self.mileage:,} miles.'


blue = car('blue', 20_000)
green = car('green', 40_000)

print(blue.out)
print(green.out)



class test:
  i=56

  def __init__(self,x):
    '''
    Initialize the class with x (str)
    '''
    self.x=x
    self.y='hello'
    self.z =  self.y + ' ' + self.x 

  def square(self,x):
    '''
    Return Squared value if x
    '''
    return x*x 


class bar:
  i=56

  def __init__(self,x):
    self.x=x
    self.y='hello'
    self.z =  self.y + ' ' + self.x 

  def __str__(self):
     return 'this class is hold "bar" type blueprints' 

  def cube(self,x):
    return x*x*x     


t = test('Me')
print(t.z) 
print(t.i) 
print(t.square(5))
t.z = 4
print(t.z)

a = test('Atul')
print(a.z)
print(a.square(9))

b = bar('Singh')
print(b)
print(b.z)
print(b.cube(5))

print(t.square.__doc__)



if t.z == a.z:
  print("Equal")
else:
  print('not equal')
import random

try:
  number = int(input("Enter an integer: "))
except ValueError:
  print("That was not an integer")  
  
  
def divide(num1, num2):
  try:
    print(num1 / num2)
  except (TypeError, ZeroDivisionError):
    print("encountered a problem")
divide(1, 'a')


try:
  line=input("Enter a string: ")
  no=int(input("Enter an index no: "))
  print(f'Index char is: {line[no]}')
except ValueError:
  print("Enter a interger value for Index")
except IndexError:
  print("Index value is greater than the String")

for i in range(10):  
  print(random.randint(3,20), end=' ')
  
# fair flipping coin
zero=0
one=0
for i in range(10_1000):  
  #no=random.randint(0,1)
  if random.randint(0,1)==0:
    zero = zero + 1 
  else:
    one = one + 1
print('zero:',str(zero))
print('one:',str(one))

# probability based flipping coin
zero=0
one=0
for i in range(10_1000):  
  #no=random.randint(0,1)
  if round(random.random()) < 1:
    zero = zero + 1 
  else:
    one = one + 1
print('zero:',str(zero))
print('one:',str(one))


# probability based flipping coin
zero=0
one=0
for i in range(10_1000):  
  #no=random.randint(0,1)
  if random.random() < 0.7:
    zero = zero + 1 
  else:
    one = one + 1
print('zero:',str(zero))
print('one:',str(one))


die=[0,0,0,0,0,0]
for i in range(10_1000):  
  #no=random.randint(0,1)
  ind=random.randint(1,6)-1
  die[ind] = die[ind] +1 
print('die:',str(die))

#########################################
flip_list=[]
for i in range(10_000):
  count=0   
  no1=random.randint(0,1)
  no2=no1
  while no1==no2:
      count=count+1
      no2=random.randint(0,1)
  flip_list.append(count)    
  #print(f'Round: {i+1},  flip: {count}, no1: {no1}, no2: {no2}')
print('Max flip:',max(flip_list))
print('Min flip:',min(flip_list))
print('Highest occured flip count:', (max(set(flip_list), key = flip_list.count)))
print('Min occured flip count:', (min(set(flip_list), key = flip_list.count)))
#----------------------------


#########################################
def win():
  region=[0.87,0.65,0.17]
  win=''
  A=0
  B=0
  for prob in region:
    if (random.random() >= prob):
      A += 1
    else:
      B += 1
  
  win = 'A' if A > B else 'B' 
  return win

total=[]
for i in range(10_000):
  total.append(win())
  
#max_win=max(set(total), key = total.count)
#min_win=min(set(total), key = total.count)
max_win='A' if total.count('A') > total.count('B') else 'B'
min_win='A' if max_win=='B' else 'B'


if max_win != min_win:
  print('Highest times winner in 10_000 simulation:', max_win)
  print('Lowest times winner in 10_000 simulation:', min_win)
else:
  print(f"In simulation, both candidate have same win count {max_win}")
#print(total)
print(total.count('A'))
print(total.count('B'))

#----------------------------


 



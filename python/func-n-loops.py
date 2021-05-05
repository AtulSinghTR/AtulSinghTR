def square(x):
  """Return the squared value

  Args:
      x (integer/float): Number
  """
  return x*x

print(square(2.3))


def convert_cel_to_far(t):
  return (t * 9/5) + 32

def convert_far_to_cel(t):
  return (t - 32) * 5/9

print(convert_cel_to_far(-40))


def invest(amount, rate, years):
  print(f'Amount invested: {amount:.2f}')
  
  cum_sum = amount
  for y in range(1, years+1):
    cum_sum = cum_sum + (cum_sum * rate)
    print(f"Year {y}: {cum_sum:.2f}")
    
invest(100, 0.05, 4)    


def factor(n):
  for i in range(1,n+1):
    (n%i ==0) and print(f"{i} is a factor of {n}")
    
factor(12)
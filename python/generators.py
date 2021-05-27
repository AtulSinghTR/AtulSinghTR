
list_a = [x*x for x in range(20) if x%2 != 0]
print(list_a)
print(type(list_a))

gen_a = (x*x for x in range(20) if x%2 != 0)
print(gen_a)
print(type(gen_a))

# looping over iterator
print('\n\nRound 1 on iterator')
for i in list_a:
  print(i, end=',')
print('\nRound 2 on iterator')
for i in list_a:
  print(i, end=',')


# looping over generator
print('\n\nRound 1 on generator')
for i in gen_a:
  print(i, end=',')
print('\nRound 2 on generator')
for i in gen_a:
  print(i, end=',')
print()

# Break & Continue

line = 'this is a big line to chec'

# if 'i' in line:
#   print('i exists.')
# else:
#   print("i doesn't exit")

# Any code in the else block after a for loop is executed only if the \
#  for loop completes without encountering a break statement.


for n in line:
  if n == 'k':
    print("k exists")
    break;
else:   # this line will always execute at the end of loop
  print('There is no k exists')

print("")
for n in line:
  if n == 'i':
    print("i exists")
    continue;
else: # this line will always execute at the end of loop
  print('Bye')
  
  
for n in range(3):
  password = input("Password: ")
  if password == "12345":
     break
  print("Password is incorrect.")
else:
  print("Suspicious activity. The authorities have been alerted.")
  
while True:
  inp=input('enter any charactor, q to quit - ')
  if inp == 'q':
    break
  print(f'you have entered : {inp}')
  
for i in range(2, 51):
  if i%3==0:
    continue
  print(i, end=' ')  

  

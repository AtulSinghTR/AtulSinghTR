
test='  The Fix should be the First      STEP to sort out any Problem   '

print('Length: ',len(test))
print('Upper: ',test.upper())
print('Lower: ',test.lower())
print('Capitalize: ',test.capitalize())
print(test.split())
print(test[:6])
print(test[:-7])
print(test[-9:])
print(test.rstrip()+'.')
print(test.lstrip()+'.')
print(test.strip()+'.')
print(test.startswith('The'))
print(test.strip().startswith('The'))
print(test.strip().endswith('lem'))


prompt = "Hey, what's up? "
user_input = input(prompt)
print("You said:", user_input[::-1])
print("You said:", ''.join(reversed(user_input)))


fname = input('Enter your first name - ')
print("You said:", fname)

passw = input("Tell me your password: ")
print('You have entered: ',passw[0].upper())


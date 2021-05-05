num = '12'
no = 12

print(num+num)
print(no+no)

print(num*3)
print(no*3)

num = input("Enter a number to be doubled: ")
doubled_num = num * 2
print(doubled_num)

no = input("Enter a number to be doubled: ")
doubled_no = int(no) * 2
print(doubled_no)

dummy_str='this is a test string to check if user entered something which match from this line'
# inp_str=input('enter a word: ')
# if dummy_str.find(inp_str.lower()) >= 0:
#   print(f"string {inp_str} exists.")
# else:
#   print(f"string {inp_str} does not exists.")


dummy_str.replace('to check', 'to CHECK')  
print(dummy_str.replace('to check', 'TO ALTERED CHECK') )
print(dummy_str)
print(dummy_str.replace('to', 'TO').replace('string', 'STRING') )

pass_w=input('Enter some text: ')
print(pass_w.replace('a','4').replace('b','8'))



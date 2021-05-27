import pathlib as p
import shutil

cur_dir = p.Path.cwd()
print(cur_dir)

tmp_dir = cur_dir / 'tmp'
tmp_dir.mkdir(exist_ok=True)

# creating file from pathlib library

file = tmp_dir / 'test1.txt'  
file.touch(exist_ok=True)

file_p = file.open(mode='r', encoding='utf-8')  # path object should exists
print(file_p)
file_p.close()

# creating file from internal library

file_o = open(file, mode='r', encoding='utf-8')
print(file_o)
file_o.close()

# To work with files, best way to use "with" 

with  open(file, mode='r', encoding='utf-8') as f:
  txt=f.read()  # read the whole file in one go. Creates problem when file is too big to fit in memory
  print(txt)
  
with  open(file, mode='r', encoding='utf-8') as f:
  for line in f.readlines():      # read line by line
    print(line)  # print func auto add a new line after printing each lines, hence the gap b/w lines
    

# Write/Append the File
  
with  open('tmp/test2.txt', mode='w', encoding='utf-8') as f:   # write mode will overrite the file if exists
  f.write('this is a test line written by python\n')
  f.write('2nd line')
  
with  open('tmp/test2.txt', mode='a', encoding='utf-8') as f:   
  f.write('\nnow, appending few lines in file \n')  # returns no of char written
  f.write('the end')
  
lines = ['\nTrying to add multiple lines via a lines array.','\nThis is the 2nd line in list.','\n& this is the last one.']
with  open('tmp/test2.txt', mode='a', encoding='utf-8') as f:   
  f.writelines(lines)  
  

# parent folders should exists to create the files.

### ----------- Read/Write CSV data

## Raw method (which has lot of problems)

data = [23,45,20,11,90,45,65,76,38]

with open('tmp/test3.csv', mode='a', encoding='utf-8') as fl:
  fl.write(str(data[0]))
  for d in data[1:]:
    fl.write(f', {d}')
    
with open('tmp/test3.csv', mode='r', encoding='utf-8') as fl:
  fl.read()
  
# best way is to use "csv" module

import csv

daily_temperatures = [[68, 65, 68, 70, 74, 72], [67, 67, 70, 72, 72, 70], [68, 70, 74, 76, 74, 73]]

with open('tmp/test4.csv', mode='w', encoding='utf-8') as fl:
  writer = csv.writer(fl)
  writer.writerows(daily_temperatures)
  
# Reading
with open('tmp/test4.csv', mode='r', encoding='utf-8') as fl:
  reader = csv.reader(fl)
  for line in reader:
    print(line)
  
  
# Reading and Writing CSV Files With Headers
with open('tmp/test5.csv', mode='r', encoding='utf-8') as fl:
  reader = csv.DictReader(fl)  # read as a dictionary of strings
  print(f"Header: {reader.fieldnames}")
  for line in reader:
    print(line)
    

people = [
{"name": "Veronica", "age": 29},
{"name": "Audrey", "age": 32},
{"name": "Sam", "age": 24},
]

with open('tmp/test5.csv', mode='w', encoding='utf-8', newline='') as fl:
  wr = csv.DictWriter(fl, fieldnames=["name", "age"])  # read as a dictionary of strings
  print(f"Header: {wr.fieldnames}")
  wr.writeheader()
  wr.writerows(people)
  
  
# Exp
with open('tmp/exc.csv', mode='r', encoding='utf-8', newline='') as fl:
  reader = csv.DictReader(fl)  # read as a dictionary of strings
  #print(reader.fieldnames) 
      
  out_dict={}
  for line in reader:
    k=line['name']
    v=line['score']
    if (k not in out_dict) or (out_dict[k] < v):
      out_dict[k] = v        
  print(out_dict)
  
  out_list=[]
  for key in out_dict.keys():
    di={}
    di['name'] = key
    di['score'] = out_dict[key]
    out_list.append(di) 
  print(out_list)

  with open('tmp/exc-out.csv', mode='w', encoding='utf-8', newline='') as fl_out:
    writer = csv.DictWriter(fl_out, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(out_list)


  
    
    
  
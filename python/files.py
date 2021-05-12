import pathlib as p

cur_dir=p.Path.cwd()

print(cur_dir)
print(p.Path.home())
print(cur_dir.is_absolute())
print(list(cur_dir.parents))

path=p.Path.home() / 'test.sh'
for dir in path.parents:
  print(dir)
print(path.parent)  # return parent dir
print(path.anchor)  # return top dir in absolute path
print(path.name)    # cur file or dir name
print(path.stem)    # file-name only
print(path.suffix)  # file ext only

print(path.exists())  # True if exists
print(cur_dir.exists())

print(path.is_file())  # True if a file

print(path.is_dir())     # True if a directory
print(cur_dir.is_dir())

#---------------------

path = p.Path.cwd() / "python" / "car.py"
print(path)
print(path.exists())
print(path.name)
print(path.parent)
print(path.is_file())

#----------------------

file = p.Path.cwd() / "tmp" / "test.py"
print(file)
dirc = p.Path.cwd() / "tmp" / "tmp-dir"
file2 = p.Path.cwd() / "tmp" / "tmp-dir" / "test.txt"
print(dirc)

file.parent.mkdir(exist_ok=True, parents=True)
dirc.mkdir(exist_ok=True, parents=True)
file2.mkdir(exist_ok=True, parents=True)

print(file.is_file())
print(file.touch())
print(file.is_file())

for i in file.parent.iterdir():
  print(i)
  
for i in file.parent.glob('*'):
  print(i)  
  
for i in file.parent.glob('*.py'):
  print(i)  
  
for i in file.parent.glob('*.txt'):
  print(i)  
  
  
new_dir = cur_dir / 'tmp'  
paths = [
new_dir / "program1.py",
new_dir / "program2.py",
new_dir / "folder_a" / "program3.py",
new_dir / "folder_a" / "folder_b" / "image1.jpg",
new_dir / "folder_a" / "folder_b" / "image2.png",
]

for path in paths:
  path.parent.mkdir(exist_ok=True, parents=True)
  path.touch()
  
print(list(new_dir.glob("*.py")))  
print(list(new_dir.glob("?older_?")))
print(list(new_dir.glob("*1.??")))
print(list(new_dir.glob("program[13].py")))

# limitation with glob and iterdir is - it will only search in the current directory at depth 0
# ** will solve this problem
print(list(new_dir.glob("**/*.txt")))

for f in list(new_dir.glob("**/*.py")):
  print(f)
  
print(list(new_dir.rglob("*.py")))         # rglob is same as glob with **


# Moving files - replace()

src = new_dir / 'test.py'
dst = new_dir / 'tmp-dir' / 'chk.py'

src.replace(dst)  # if destination file exist, it will overwrite without warning

# can use to rename directory or files

src = new_dir / 'tmp-dir'
dst = new_dir / 'temp-dir'

src.replace(dst)


# Deleting files/folders
# use unlink() method

file = new_dir / 'program1.py'
print(file.exists())
file.unlink(missing_ok=True)  # if file is missing, it's ok
print(file.exists())

# To delete a folder use rmdir() method but dir should be empty before

del_dir = new_dir / 'folder_a'
try:
  del_dir.rmdir()
except Exception as e:
  print(f"Dir Deletion Error - {e}")
  
for file in list(del_dir.rglob('*.*')):  # search all file with extension
  file.unlink(missing_ok=True)
for dir in  list(del_dir.rglob('*')):   # after deleting all files, deleting child directory
  dir.rmdir() 
del_dir.rmdir()                         # deleting parent dir


# this all can be done easily via a library shutil
del_dir = new_dir / 'temp-dir'

import shutil 
shutil.rmtree(del_dir)  


#------------- 

new_dir = cur_dir / 'tmp'  
paths = [
new_dir / "img1.jpg",
new_dir / "img2.gif",
new_dir / "folder_a" / "img3.png",
new_dir / "folder_a" / "folder_b" / "img4.jpg",
]

# Creating all the files and folders
for path in paths:
  path.parent.mkdir(exist_ok=True, parents=True)
  path.touch()
  
img_dir = new_dir / 'img'
img_dir.mkdir(exist_ok=True, parents=True)

for file in new_dir.rglob('*.*'):
  file_name = file.name
  out_file = img_dir / file_name
  file.replace(out_file)
  

# Deleting the folder structure
shutil.rmtree(new_dir)  
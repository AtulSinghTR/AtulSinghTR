import sys
x=(1)
print(type(x))

x=(1,)
print(type(x))

# Common array func work with tuple also
tup_1=(1,2,3,4,5)
print('length:', len(tup_1))
print('Slicing:', tup_1[:2])

# tuples are immutables
try:
  tup_1[0] = 9
# except:
#   print(sys.exc_info()[0], sys.exc_info()[1])
except Exception as e:
    print(e)

# tuples are iterables
for i in tup_1:
  print(i, end=' ')    
    
# Packing and Unpacking of tuples 
tup_2 = 6, 9, 8
print(tup_2)
print(type(tup_2))

a,b,c = tup_2
print(a,b,c)
print(type(a))

# Exer
cardinal_numbers= "first", "second" , "third"
print(cardinal_numbers[1])
pos1, pos2, pos3 = cardinal_numbers
'2nd' in cardinal_numbers
print(cardinal_numbers[1:])


### 
### List
###
universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]


def enrollment_stats(university):
  student_enrolled=[]
  tuition_fees=[]
  for un in university:
    student_enrolled.append(un[1])
    tuition_fees.append(un[2])
  return student_enrolled,tuition_fees

def mean(lst):
  return sum(lst) / len(lst)

#def median(lst):
    

enroll,fee = enrollment_stats(universities)
print(f"Total Students: {sum(enroll):,}")
print(f"Total Tuition: $ {sum(fee):,}")

print(f"Students Mean: {mean(enroll):,.2f}")


#========

Nouns=["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
Verbs= ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
Adjectives= ["furry", "balding", "incredulous", "fragrant","exuberant", "glistening"]
Prepositions= ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
Adverbs= ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

import random
def random_char(choice):
  return random.choice(choice)
  

print(f"A {adj1} {noun1}")
print(f"{A/An} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}")
print(f"{adverb1}, the {noun1} {verb2}")
print(f"the {noun2} {verb3} {prep2} a {adj3} {noun3}")


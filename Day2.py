# formatted string
#
# expected output: shahidul [islam] is a coder.

first = 'shahidul'
last = 'islam'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)

# ---------------------------------
# string method
# ---------------------------------

course = 'python for beginners SHAHIDUL'
print(len(course))
print(course.upper())
print(course.lower())
print(course.title())       #capitalize each words
print(course.find('p'))
print(course.find('P'))   #P is nowhere in the code

print(course.replace('beginners', 'noobmaster'))
print(course.replace('beginn', 'noobmaster'))
print(course.replace('begi', 'jet'))

print('python' in course)
print('Python' in course) #case sensitive

#
# ---------------------------------------------
#
#
# arithmetic operations
# ----------------------------------------------

print (10/3)        #with floating point val
print((10 // 3))    #no floating point value
print(10%3)         #remainder
print(10*3)         #multiply
print(10**3)        #to the power
# -------------------------------------------
# augmented/incremented
x = 10
x = 5 + x
print(x)

y = 10
y += 4
print(y)

z = 10
z -=3
print(z)
# --------------------------------------------

x1 = 10 + 3 * 4 / 2
print(x1)
x2 = 10 + 4 * 2
print(x2)

# order of operations:
# exponentiation 2**3
# multiplication or division
# addition or substraction

x3 = 10 + 3 * 2 ** 3
print(x3)

x4 = (2+3) * 10 - 3
print(x4)
# -----------------------------------
#
# math funtions
# ------------------------------------

x1 = 2.4
print(round(x1))

x2 = 2.5
print(round(x2))

x3 = 2.6
print(round(x3))

print(abs(-3.1416))

# -------------------------------------
# module : it is a separate file with some reusable code.
# we use these to organize our code into different files.
# -------------------------------------------------

import math

print(math.ceil(2.9))
print(math.floor(2.9))

# -------------------------------------------------
# documentation
# https://docs.python.org/3/library/math.html
# ------------------------end of day 2 practice-------------------
# ---------------------------30/may/2024--------------------------
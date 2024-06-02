#if statements

is_hot = True
if is_hot:
    print("it's a hot day")
    print("drink plenty of water")
print("enjoy your day")
print('----------------------')

is_hot = False
if is_hot:
    print("it's a hot day")
print("enjoy your day")
print('----------------------')

is_hot = False #change the value to false and see the difference
is_cold = True # change to false and see the difference
if is_hot:
    print("it's a hot day")
    print("drink plenty of waters")
elif is_cold:
    print("it's a cold day")
    print("wear warm clothes")
else:
    print("it's a lovely day")
print("enjoy your day")
#---------------------------end of day 3-------------------------
#-------------------------date 1-june-2024--------------------------
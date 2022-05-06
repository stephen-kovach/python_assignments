

# 1.  Basic.  Print all integers from 0 to 150

# for x in range(0, 151):
#     print(x)

# 2.  Multiples of Five:  Print all the multiples of 5 from 5 to 1,000

# for x in range (5, 1001):
#     if x % 5 == 0:
#         print(x)

# 3.  Counting, the Doojo Way.  Print integers 1 to 100.  If divisible by five, print "Coding" if divisible by 10, print "Codiing Dojo"

# for x in range (1, 101):
#     if x % 10 == 0:
#         print('Coding Dojo')
#     elif x % 5 ==0:
#         print('Coding')
#     else: print(x)

# 4.  Whoa. That sucker's huge.  Add odd integers from 0 to 500,000 and print the final sum


sum = 0
for x in range(1, 500001):
    if x % 2 != 0:
        sum = sum + x
        print('x is equal to ' + str(x))
        print('sum is equal to', sum)

# 5 Countdown by Fours

for x in range (2018, 0, -4):
    print(x)

# Flexible Counter

low_num = 2
high_num = 19
mult = 5

for x in range (low_num, high_num):
    if x % mult == 0:
        print(x)
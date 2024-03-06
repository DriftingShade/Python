# 1. Basic - Print all integers from 0 to 150.
for i in range(151):
    print(i)


# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(0, 1005, 5):
    print(i)


# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1, 101, 1):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)


# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
minimum = 0
maximum = 500000
Oddtotal = 0

for number in range(minimum, maximum + 1):
    if number % 2 != 0:
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from {0} to {1} = {2}".format(minimum, maximum, Oddtotal))

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
number = 2018
while number > 0:
    print(number)
    number = number - 4


# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def flex_count(low, high, mult):
    for i in range(low, high):
        if i % mult == 0:
            print(i)


flex_count(2, 27, 3)

# an intiger is a number and a float is a decimal.
num = .3

print(type(num))

# so in python 3, 3 / 2 = 1.5 while in python 2.whatever, it would equal 1 because it would drop the decimal.

# to floor a division, you add two division signs
print(3 // 2)  # so this equals 1

# use a double ** to get powers

print(3 ** 2)   # so this equals 9

# this is a 'modulus' % and it gives us the remainder after a division
print(3 % 2)    # so this equals 1
# if you do a mod 2 you know you have an even number. this is an important thing to know in python i guess.

# this tells us the value of the intiger, without the negative designation.
print(abs(-3))

# this prints a rounded version of a decimal(float)
print(round(3.7555))

# how many do we want to round to?
print(round(3.733, 2))  # goes to the second place so hundreths here.

# this will produce a boolean:

num = 1
num2 = 2

print(num == num2)  # so false

num01 = '100'
num2 = '200'

# this is how to cast a string of a number to an int
num01 = int(num01)
num2 = int(num2)

print(num01 + num2)

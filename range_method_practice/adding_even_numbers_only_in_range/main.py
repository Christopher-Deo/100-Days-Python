# Create a for loop using the range function that loops over all numbers between and including 1 to 100 and add up
# all the even numbers

# Will require range() and modulo operator

#  set up accumulator value
total = 0
# declare for loop with range
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)

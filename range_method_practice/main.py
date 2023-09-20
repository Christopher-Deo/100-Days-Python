# for loop with Range
# print out all numbers between 1 and 100
# for number in range(0, 101):  # range will not include last number. Since we want 100, we have to specify 101.
#     print(number)
#

# Now loop through the range and add all the numbers together to create the sum of all numbers in the range between 1
# and 100 (answer: 5050)

#  need an accumulator value
total = 0
# set up for loop with range
for number in range(1, 101):
    total += number  # getting total and adding the next number to it.
print(total)

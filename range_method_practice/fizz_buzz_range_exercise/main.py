# Create a program that prints each number between 1 and 100, including both.
# If the number is divisible by 3, instead of printing the number, it should print "Fizz"
# If the number is divisible by 5, instead of printing the number, it should print "Buzz"
# if the number is divisible by both 3 and 5, it should print "FizzBuzz"

#  requirements
# for loop with range()
# modulo operator usage
# conditionals such as if statements
# print each number or term to the console as appropriate

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

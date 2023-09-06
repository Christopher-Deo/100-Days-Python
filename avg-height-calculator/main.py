# Initialize an empty list to store the heights
student_heights = []

# Get the number of students as input
num_students = int(input("Enter the number of students: "))

# Loop to collect the heights from the user
for i in range(num_students):
    height = float(input(f"Enter the height of student {i + 1} in centimeters: "))
    student_heights.append(height)

# Initialize variables to calculate the sum and count
total_height = 0
count = 0

# Loop to calculate the sum of heights
for height in student_heights:
    total_height += height
    count += 1

# Calculate the average height
average_height = total_height / count

# Round the average height to two decimal places
average_height = round(average_height, 2)

# Display the result
print(f"The average height of {num_students} students is {average_height} centimeters.")

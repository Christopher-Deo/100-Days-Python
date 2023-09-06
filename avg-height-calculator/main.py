# Initialize an empty list to store the heights
student_heights = []

# Get the heights from the user, terminated by an empty input
while True:
    height_input = input("Enter the height of a student in centimeters (or press Enter to finish): ")

    if height_input == "":
        break

    try:
        height = float(height_input)
        student_heights.append(height)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Check if the list is empty
if not student_heights:
    print("No heights were entered.")
else:
    # Initialize variables to calculate the sum and count
    total_height = 0
    count = 0

    # Loop to calculate the sum of heights
    for height in student_heights:
        total_height += height
        count += 1

    # Calculate the average height
    average_height = total_height / count

    # Round the average height to the nearest whole number
    average_height = round(average_height)

    # Display the result
    print(f"The average height of the students is {average_height} centimeters.")

# Get width and length from the user
widthR = float(input("Enter the width of the rectangle: "))
lengthR = float(input("Enter the length of the rectangle: "))

# Calculate area and circumference
areaR = widthR * lengthR
circumferenceR = 2 * (widthR + lengthR)

# Display the results
print(f'For a rectangle with width {widthR} and length {lengthR}, the area is {areaR} and the circumference is {circumferenceR}')

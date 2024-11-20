import argparse

# Set up argparse to accept the radius as a command-line argument
parser = argparse.ArgumentParser(description='Calculate the area and circumference of a circle.')
parser.add_argument('radiusC', type=float, help='The radius of the circle')

# Parse the command line arguments
args = parser.parse_args()

# Calculate the area and circumference of the circle
areaC = 3.14 * args.radiusC**2
circumferenceC = 2 * 3.14 * args.radiusC

# Display the results
print(f'A circle with radius {args.radiusC} has a circumference {circumferenceC} and area {areaC}')

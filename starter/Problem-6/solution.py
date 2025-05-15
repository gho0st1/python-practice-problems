### Problem-6: Write a function named "isLandscape" that takes 2 numbers (image width and height) as arguments and the function returns Landscape if the image width has a higher value than height. Returns Portrait otherwise

def isLandscape(height: int, width: int) -> str:
	return "Portrait" if height > width else "Landscape"

height = 5
width = 8

# height = int(input("Enter image height: "))
# width = int(input("Enter image width: "))

print(f"The image is a {isLandscape(height, width)}")
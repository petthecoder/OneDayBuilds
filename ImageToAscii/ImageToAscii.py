import sys
from PIL import Image
from pathlib import Path

# Read image
route = sys.argv[1]
image = Image.open(route)
new_image_size = 150

# Resize image
width = image.width
height = image.height
image = image.resize((new_image_size, int(height/width * new_image_size * 0.5)))


# Turn grey and get pixels
image = image.convert('L')
pixels = image.getdata()


# Replace pixel values
chars = [" ",".",":","º","*","!","o","O","#","@"]
converted_image = [chars[int(pixel/26)] for pixel in pixels]

# Separate string into different lines
converted_image = ''.join(converted_image)
total_pixels = len(converted_image)
final_image = [converted_image[i:i + new_image_size] for i in range(0, total_pixels, new_image_size)]
final_image = "\n".join(final_image)
print(final_image)

# Write in a .txt file
with open(Path(route).stem + ".txt", "w") as f:
 f.write(final_image)
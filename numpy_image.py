import numpy as np
from PIL import Image

img = Image.open("img/dots.png")
img_arr = np.array(img)
print(img_arr) # Convert image to numpy array and print it









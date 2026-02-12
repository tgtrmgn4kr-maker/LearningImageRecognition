import cv2
from pathlib import Path
from os import path

img_path = path.join(Path(__file__).resolve().parent,'img/arch.jpg')

img = cv2.imread(img_path)

if img is None:
    print("Reading image failed")

else:
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert to grayscale
    cv2.imshow("Gray Image", gray_img)
    cv2.imshow("Original Image", img)

    cv2.waitKey(0) # Wait for any key press to close the windows
    cv2.destroyAllWindows()


LearningImageRecognition
===
This repository is for recording my learning progress

## What I practiced
- Using `PIL.Image()` to put watermark on a picture
- Using `numpy` to convert image to numpy array
- Using `cv2.cvtColor()` (OpenCV) to convert image to grayscale 
- Using `cv2.VideoCapture()` (OpenCV) to use camera
- Using a model to check if there is any faces exists in the frame
- Using `cv2.waitKey()` to wait for user input the button to quit the program

## Notes
- The accuracy of recognizing faces depends on the quality of the model
- I think that the easiest way to figure out the path of the file is using `path.join(Path(__file__).resolve().parent,"[filename]")`

## Files and Directories
### Directories
- `img`: to store the example images
- `models`: to store the face recognition model

### Files
- `gray_image.py`: convert a image into grayscale
- `watermark_img.py`: put watermarks on images
- `capture_image.py`: use camera and make the frame gray because it is easier to let model recognize if there are faces
 
















































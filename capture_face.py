import cv2
import sys
from os import path
from pathlib import Path

haar_file = path.join(Path(__file__).resolve().parent,"models/haar_face.xml")

try:
    face_haar = cv2.CascadeClassifier(haar_file) # Load the pre-trained model for face detection
except:
    print("Error occurred when loading the model")
    sys.exit(1)

if face_haar.empty():
    print("Error occurred when loading the model")
    sys.exit(1)

cap = cv2.VideoCapture(0) # 0 is the default camera, change if you have multiple cameras

if not cap.isOpened():
    print("The camera cannot be opened")
    sys.exit(1)

while True:
    ret, frame = cap.read() # Capture frame-by-frame

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_haar.detectMultiScale(gray, 
                                       scaleFactor=1.2,
                                       minNeighbors=6,
                                       minSize=(30,30)
                                       ) # Detect faces

    for box in faces:
        cv2.rectangle(frame, box, (255,0,0), 2)  # Draw rectangle around the faces

    cv2.imshow('Face', frame) # window name/ frame to display

    if cv2.waitKey(1) == 27: # ESC key to exit
        print("Exit...")
        break


cap.release()
cv2.destroyAllWindows()


  









































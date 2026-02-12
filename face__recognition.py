import face_recognition
from PIL import Image, ImageDraw
from os import path
from pathlib import Path

path = path.join(Path(__file__).resolve().parent, "img/photo.jpg") # 已知人臉圖片的資料夾路徑

img = face_recognition.load_image_file(path)
face_list = face_recognition.face_landmarks(img)

print(f"There are {len(face_list)} faces in this image.")

pil_img = Image.fromarray(img)
draw = ImageDraw.Draw(pil_img)

for marks in face_list:
    for f in marks.keys():
        print(f"{f} : {marks[f]}")
        draw.line(marks[f], width=5)    

pil_img.show()

input("Press Enter to exit...")

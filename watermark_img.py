import os
from PIL import Image

def main(src_dir='img', 
         save_dir='thumb', 
         logo_dir='img', 
         logo_img='swf_logo.png',
         size=600,
         margin=20):
    
    thumb_size = (size,size) # size of new image
    logo_path = os.path.join(logo_dir,logo_img) # Open logo file

    logo = Image.open(logo_path)
    logo_w, logo_h = logo.size

    for i in os.listdir(src_dir):
        if i.endswith('.jpg'):
            img_path = os.path.join(src_dir, i)

            img = Image.open(img_path) # Open target files
            img.thumbnail(thumb_size)
    
            img_w, img_h = img.size

            x = img_w - logo_w - margin
            y = img_h - logo_h - margin

            img.paste(logo, (x, y), logo) # image/coordinate/mask type

            save_path = os.path.join(save_dir, i)
            img.save(save_path, quality=80)

if __name__ == "__main__":
    main()




























































from PIL import ImageGrab
import os

BOX = (536,326,1390,806) # bounding box for Minecraft

def screenGrab(time, dst_dir, box=BOX):
    im = ImageGrab.grab(box)

    img_name = "image_" + time + ".png"
    im.save(os.path.join(dst_dir, img_name), "PNG")


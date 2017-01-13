from PIL import Image
from PIL import ImageOps
import sys
def einberz(image):
    img = Image.open(image)
    img_w, img_h = img.size
    bg = Image.new('RGB', (img_w, img_h), (255,255,255))
    img = ImageOps.fit(img,(img_w / 32, img_h / 32),0,0,(0,0))
    img = ImageOps.grayscale(img)
    print(img_w)
    print(img_w/32)
    pix = img.load()
    for i in range(0,img_h/32):
        for j in range(0,img_w/32):
            berz = Image.open("berzan-logga.jpg")
            value = pix[j,i]
            size = (int(-value/8)+45,int(-value/8)+45)
            border = -list(size)[0]/32
            berz = ImageOps.fit(berz, size, 0, 0, (0.0, 0.0))
            bg.paste(berz,(j*32,i*32))
    bg.save("out.jpg")
print "enter your image's filename:"
filename = raw_input()
einberz(filename)

from PIL import Image
from PIL import ImageOps
def einberz(image):
    bg = Image.new('RGB', (1280, 2272), (255,255,255))
    img = Image.open(image)
    img = ImageOps.fit(img,(40,71),0,0,(0,0))
    pix = img.load()
    for i in range(0,71):
        for j in range(0,40):
            berz = Image.open("berzan-logga.jpg")
            value = list(pix[j,i])
            size = (int(-value[0]/8+45),int(-value[0]/8+45))
            border = -list(size)[0]/32
            berz = ImageOps.grayscale(berz)
            berz = ImageOps.fit(berz, size, 0, 0, (0.0, 0.0))
            bg.paste(berz,(j*32,i*32))
    bg.save("out.jpg")
    img.save("out2.jpg")
einberz("wow.jpg")

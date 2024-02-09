

import image

og = image.FileImage("cat.png")

width = og.getWidth()
height = og.getHeight()

myimagewindow = image.ImageWin((width*2),(height*2), "Cats")


imgInvert = image.FileImage("cat.png")
grayImg = image.FileImage("cat.png")
colImg = image.FileImage("cat.png")

#makes all the blue in image gray
for row in range(height):
    for col in range(width):
        t = imgInvert.getPixel(col, row)

        #newred = 255 - t.getRed()
        #newgreen = 255 - t.getGreen()
        #newblue = 255 - t.getBlue()
        gray = int((t.getRed() + t.getGreen() + t.getBlue())/3)
        #newPixel0 = image.Pixel(newred, newgreen, newblue)
        newPixel0 = image.Pixel(t.getRed(), t.getGreen(), gray)
        imgInvert.setPixel(col, row, newPixel0)


#grayscales image
for row in range(height):
    for col in range(width):
        g = grayImg.getPixel(col, row)

        gray = int((g.getRed() + g.getGreen() + g.getBlue())/3)

        newPixel2 = image.Pixel(gray, gray, gray)

        grayImg.setPixel(col, row, newPixel2)


#makes all red in image gray
for row in range(height):
    for col in range(width):
        r = colImg.getPixel(col, row)

        gray = int((r.getRed() + r.getGreen() + r.getBlue())/3)

        newPixel = image.Pixel(gray, r.getGreen(), r.getBlue())

        colImg.setPixel(col, row, newPixel)




og.setPosition(width,height)
og.draw(myimagewindow)

imgInvert.setPosition(width,0)
imgInvert.draw(myimagewindow)

grayImg.setPosition(0, 0)
grayImg.draw(myimagewindow)

colImg.setPosition(0,height)
colImg.draw(myimagewindow)

myimagewindow.exitOnClick()
import image

img1 = image.FileImage('soupcan.png')
img2 = img1.copy()
img3 = img1.copy()
img4 = img1.copy()
img5 = img1.copy()
img6 = img1.copy()

width = img1.get_width()
height = img1.get_height()

win = image.ImageWin(width*3, height*3, "And5y Warhol")


img1.draw(win)
img2.setPosition(width, 0)
img3.setPosition(width*2, 0)
img4.setPosition(0, height)
img5.setPosition(width, height)
img6.setPosition(width*2, height)

img2.draw(win)
img3.draw(win)
img4.draw(win)
img5.draw(win)
img6.draw(win)

win.exitOnClick()
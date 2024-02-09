import math
import image

class ComplexNumber:

    def __init__(self, inita, initb):
        self.a = inita
        self.b = initb

    def RealPart(self):
        return self.a

    def ImagPart(self):
        return self.b
    
    def Conjugate(self):
        return ComplexNumber(self.a, -self.b)
    
    def __str__(self):
        if self.b >= 0:
            return str(self.a) + " + " + str(self.b) + "i"
        else:
            return str(self.a) + " - " + str(-self.b) + "i"

    def __add__(self, z):
        return ComplexNumber(self.a + z.a, self.b + z.b)

    def __sub__(self, z):
        return ComplexNumber(self.a - z.a, self.b - z.b)

    def __mul__(self, z):
        temp1 = self.a*z.a - self.b*z.b
        temp2 = self.a*z.b + self.b*z.a
        return ComplexNumber(temp1, temp2)
    
    def Norm(self):
        return math.sqrt(self.a**2 + self.b**2)
    
    def Normsq(self):
        return self.a**2 + self.b**2

    def __truediv__(self, z):
        denom = z.Normsq()
        ans = self * z.Conjugate()
        return ComplexNumber(ans.a / denom, ans.b / denom)
    
canvas = image.EmptyImage(400,400)

width = canvas.getWidth()
height = canvas.getHeight()

win = image.ImageWin(width,height,"Factal Warhol")


for row in range(int(height/2)):
    for col in range(int(width/2)):

        z0 = ComplexNumber((col-(width/4))/100, ((height/4)-row)/100)
        zn = z0

        colorn = 255
        for i in range(255):
            if zn.Normsq() > 4:
                colorn = i  
                break
            zn = zn*zn + z0

        pixel = canvas.getPixel(col, row)
        pixel.setRed(colorn)
        pixel.setGreen(0)
        pixel.setBlue(0)
        canvas.setPixel(col, row, pixel)
canvas.draw(win)

for row in range(int(height/2)):
    for col in range(int(width/2)):

        z0 = ComplexNumber((col-(width/4))/100, ((height/4)-row)/100)
        zn = z0
        
        colorn = 255
        for i in range(255):
            
            if zn.Normsq() > 4:
                colorn = i  
                break
            zn = zn*zn*zn + z0

        pixel = canvas.getPixel(col+int(width/2), row)
        pixel.setRed(0)
        pixel.setGreen(colorn)
        pixel.setBlue(0)
        canvas.setPixel(col+int(width/2), row, pixel)
canvas.draw(win)

for row in range(int(height/2)):
    for col in range(int(width/2)):

        z0 = ComplexNumber((row-(width/4))/100, ((height/4)-col)/100)
        zn = z0
        
        colorn = 255
        for i in range(255):
            
            if zn.Normsq() > 4:
                colorn = i  
                break
            zn = zn*zn*zn +z0

        pixel = canvas.getPixel(col, row+int(height/2))
        pixel.setRed(0)
        pixel.setGreen(colorn)
        pixel.setBlue(colorn)
        canvas.setPixel(col, row+int(height/2), pixel)
canvas.draw(win)

for row in range(int(height/2)):
    for col in range(int(width/2)):

        z0 = ComplexNumber((col-(width/4))/100, ((height/4)-row)/100)
        zn = z0
        
        colorn = 255
        for i in range(255):
            
            if zn.Normsq() > 2:
                colorn = i
                break
            zn = zn*zn - z0
            #zn = zn*zn*zn +z0

        pixel = canvas.getPixel(col+int(width/2), row+int(height/2))
        pixel.setRed(colorn)
        pixel.setGreen(0)
        pixel.setBlue(colorn)
        canvas.setPixel(col+int(width/2), row+int(height/2), pixel)


canvas.draw(win)

print("finish")
win.exitOnClick()   
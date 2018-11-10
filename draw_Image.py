
from PIL import ImageTk, Image, ImageDraw, ImageFilter
import PIL
from Tkinter import *
import os


width = 256
height = 256

white = (255, 255, 255)
black=(0,0,0)


global cv
def save():
    filename = "image.png"
    image1.save(filename)


def delteAll():
	cv.delete(ALL)
	
	os.remove("image.png")
	
	
	

def paint(event):
    # python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval(x1, y1, x2, y2, fill="white",width=20)
    draw.line([x1, y1, x2, y2],fill="white",width=10)

root = Tk()
root.title("Digits Recognition")


# Tkinter create a canvas to draw on
cv = Canvas(root, width=width, height=height, bg='white')

cv.pack()

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = PIL.Image.new("RGB", (width, height), black)
draw = ImageDraw.Draw(image1)



cv.pack(expand=YES, fill=BOTH)
cv1=cv.bind("<B1-Motion>", paint)


button=Button(text="Save",command=save)
buttondelete=Button(text="Clear",command=delteAll)


button.pack()
buttondelete.pack()
root.mainloop()

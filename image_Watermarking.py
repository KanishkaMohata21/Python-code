from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk

file = filedialog.askopenfilename(initialdir=r"", title="Select an Image: ")

def image_Watermarking(image, mark):
    opened_image = Image.open(image)
    image_width, image_height = opened_image.size
    draw = ImageDraw.Draw(opened_image)
    
    font_size = int(image_width / 10)
    font = ImageFont.truetype("arial.ttf", font_size)
    
    x, y = int(image_width/2), int(image_height)
    
    draw.text((x, y), mark, font=font, fill="#fff", stroke_width=5, stroke_fill="#222", anchor="ms")
    
    opened_image.show()

window = Tk()
image_Watermarking(file, "Kanishka")
window.mainloop()

import colorgram
import turtle as t
import random
import turtle as t
import random

# this code was used to extract colour for image1
rgb_colors=[]
colors=colorgram.extract(r"C:\Users\ssc\Desktop\100.days.of.code\painting\image1.png" ,30)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)


t.colormode(255)
tim=t.Turtle()
tim.speed("fastest")

color_list=[(236, 80, 224), (197, 71, 7), (195, 13, 164), (201, 15, 75), (231, 132, 54), (110, 216, 179), (217, 101, 163), (27, 168, 105), (35, 109, 186), (19, 168, 29), (13, 66, 23), (212, 177, 135), (233, 7, 223), (199, 132, 33), (13, 212, 183), (230, 199, 
166), (126, 162, 189), (8, 28, 49), (40, 77, 132), (128, 232, 219), (58, 25, 12), (67, 7, 22), (114, 210, 90), (146, 199, 216), (179, 8, 17), (233, 34, 66)]  

tim.hideturtle(
    
)
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for i in range(1,101):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if i%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen=t.Screen()
screen.exitonclick()
#import colorgram
import random
import turtle as t
# rgb_colors = []
# colors = colorgram.extract("hirts_dots.jpg",30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
# configuración original canvwidth = 400, canvheighth = 300
color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]
jim = t.Turtle()
t.colormode(255)
#tim.speed()
#nextposition function
# empezar en una esquina, tamaño del canvas
t.screensize(500,500)
jim.up()
inicial_x = -400
inicial_y = -300
jim.setpos(inicial_x, inicial_y)
largo = 10
alto = 10
jim.speed(0)

#hace una linea
#subir regresar hacer una l[inea
#medir el espacio
for a in range(alto):
    for l in range(largo):
       jim.forward(72)
       jim.color(random.choice(color_list))
       #print(color)
       jim.dot(30)
    inicial_y += 70
    jim.setpos(inicial_x, inicial_y)
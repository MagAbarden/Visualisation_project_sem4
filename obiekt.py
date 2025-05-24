from vpython import *
import numpy as np

canprint = False #Check if you can start printing figures
ifcenter = False #Check for alignment of the printer head
figurechoice = 0 #Check which figure

i = 0
j = 0
go_value = 0.1

#Simulation captions
scene.caption = """Right button drag or Ctrl-drag to rotate "camera" to view scene.
To zoom, drag with middle button or Alt/Opti`on depressed, or use scroll wheel.
    On a two-button mouse, middle is left + right.
Shift-drag to pan left/right and up/down.

Make horizontal movement with arrow keys
Make vertical movement with "w" and "s"
"""
text(pos=vec(0, 0, 6), text='NORTH', align='ifcenter', color=color.white, up=vec(0,0,1), axis=vector(-1,0,0))

#Printer's support visualisation
main_plane = box(pos=vec(0, 0, 0), length=10, height=0.1, width=10, color=color.white)

sw_support = box(pos=vec(-4.9, 2.5, -4.9), length=0.2, height=5, width=0.2, color=color.orange)
se_support = box(pos=vec(4.9, 2.5, -4.9), length=0.2, height=5, width=0.2, color=color.orange)
nw_support = box(pos=vec(-4.9, 2.5, 4.9), length=0.2, height=5, width=0.2, color=color.orange)
ne_support = box(pos=vec(4.9, 2.5, 4.9), length=0.2, height=5, width=0.2, color=color.orange)

n_support = box(pos=vec(4.9, 5, 0), length=0.2, height=0.2, width=10, color=color.orange)
s_support = box(pos=vec(-4.9, 5, 0), length=0.2, height=0.2, width=10, color=color.orange)
w_support = box(pos=vec(0, 5, 4.9), length=10, height=0.2, width=0.2, color=color.orange)
e_support = box(pos=vec(0, 5, -4.9), length=10, height=0.2, width=0.2, color=color.orange)

#Printer's moving elements visualisation
support_z = box(pos=vec(0, 5, 0), length=9.6, height=0.2, width=0.2, color=color.blue)
support_x = box(pos=vec(0, 5, 0), length=0.2, height=0.2, width=9.6, color=color.blue)

crane = box(pos=vec(0, 5.2, 0), length=0.2, height=5, width=0.2, color=color.red)
head = cone(pos=vec(0, 2.7, 0), axis=vec(0, -0.2, 0), radius=0.1, color=color.red, make_trail=False, trail_radius = 0.2)

#Custom print
def printfun():
        if customprint.text == 'Start printing':
                if head.pos.y < 0.2:
                        head.make_trail = True
                        customprint.text = "Stop printing"
        else:
                head.make_trail = False
                customprint.text = "Start printing"
                
def clearfun():
        if customprint.text == 'Start printing':
                head.clear_trail()

def colorfun(evt):
        if evt.text == 'Red':
                head.trail_color=color.red
        elif evt.text == 'Green':
                head.trail_color=color.green
        elif evt.text == 'Blue':
                head.trail_color=color.blue

customprint = button (bind = printfun, text = "Start printing")

clearprint = button (bind = clearfun, text = "Clear objects")

redbutton = radio(bind=colorfun, text='Red', name='colors', checked=True)
greenbutton = radio(bind=colorfun, text='Green', name='colors')
bluebutton = radio(bind=colorfun, text='Blue', name='colors')

wtext(text="\n\n")      

#Preset figure choice and print
def whichfigure(evt):
        global figurechoice
        if evt.text == 'Rectangle':
                figurechoice = 0
        elif evt.text == 'Spring':
                figurechoice = 1
        elif evt.text == 'Ball  ':
                figurechoice = 2

def buildorder():
        global ifcenter
        ifcenter = True
        
rectangle = radio(bind=whichfigure, text='Rectangle', name='figures', checked=True)
spring = radio(bind=whichfigure, text='Spring', name='figures')
ball = radio(bind=whichfigure, text='Ball  ', name='figures')

build = button (bind = buildorder, text = "build")

#Main loop
while True:
        rate(30)
        
        #Printer controls
        key = keysdown()
        if key:
                if 'up' in key:
                        if support_z.pos.z < 4.65:
                                support_z.pos.z += 0.1
                                crane.pos.z += 0.1
                                head.pos.z += 0.1
                elif 'down' in key:
                        if support_z.pos.z > -4.65:
                                support_z.pos.z += -0.1 
                                crane.pos.z += -0.1
                                head.pos.z += -0.1
                if 'left' in key:
                        if support_x.pos.x < 4.65:
                                support_x.pos.x += 0.1
                                crane.pos.x += 0.1
                                head.pos.x += 0.1
                elif 'right' in key:
                        if support_x.pos.x > -4.65:
                                support_x.pos.x += -0.1 
                                crane.pos.x += -0.1
                                head.pos.x += -0.1
                if 'w' in key:
                        if head.pos.y < 4.6:
                                crane.pos.y += 0.1
                                head.pos.y += 0.1
                elif 's' in key:
                        if head.pos.y > 0.2:
                                crane.pos.y += -0.1
                                head.pos.y += -0.1
        
        #Centering printer head
        if ifcenter == True:
                if head.pos.y > 0.2:
                        crane.pos.y += -0.05
                        head.pos.y += -0.05
                if head.pos.z > 0:
                        support_z.pos.z += -0.05
                        crane.pos.z += -0.05
                        head.pos.z += -0.05
                elif head.pos.z < 0:
                        support_z.pos.z += 0.05
                        crane.pos.z += 0.05
                        head.pos.z += 0.05
                if head.pos.x > 0:
                        support_x.pos.x += -0.05 
                        crane.pos.x += -0.05
                        head.pos.x += -0.05
                elif head.pos.x < 0:
                        support_x.pos.x += 0.05
                        crane.pos.x += 0.05
                        head.pos.x += 0.05
                if -0.1 < head.pos.x < 0.1 and -0.1 < head.pos.z < 0.1 and head.pos.y < 0.3:
                        canprint = True
                        ifcenter = False
                        head.make_trail = True
        #Start printing
        if canprint == True:
                if figurechoice == 0: #Rectangle
                        if j < 16 :
                                if i < 16:
                                        support_x.pos.x += go_value
                                        crane.pos.x += go_value
                                        head.pos.x += go_value
                                        i += 1
                                if i == 16:
                                        support_z.pos.z += 0.1
                                        crane.pos.z += 0.1
                                        head.pos.z += 0.1
                                        i = 0
                                        go_value = -go_value
                                        j += 1
                        if 15 < j < 24:
                                if i < 16:
                                        support_x.pos.x += 0.1
                                        crane.pos.x += 0.1
                                        head.pos.x += 0.1
                                elif 15 < i < 32:
                                        support_z.pos.z += -0.1
                                        crane.pos.z += -0.1
                                        head.pos.z += -0.1
                                elif 31 < i < 48:
                                        support_x.pos.x -= 0.1
                                        crane.pos.x -= 0.1
                                        head.pos.x -= 0.1
                                elif 47 < i < 64:
                                        support_z.pos.z -= -0.1
                                        crane.pos.z -= -0.1
                                        head.pos.z -= -0.1        
                                i += 1
                                if i == 64:
                                        crane.pos.y += 0.2
                                        head.pos.y += 0.2
                                        i = 0
                                        j += 1
                        if 23 < j < 40:
                                if i < 16:
                                        support_x.pos.x += go_value
                                        crane.pos.x += go_value
                                        head.pos.x += go_value
                                        i += 1
                                if i == 16:
                                        support_z.pos.z += -0.1
                                        crane.pos.z += -0.1
                                        head.pos.z += -0.1
                                        i = 0
                                        go_value = -go_value
                                        j += 1
                        if j == 40:
                               head.make_trail = False
                               canprint = False
                               i = 0
                               j = 0
        
                if figurechoice == 1: #Spring
                        if j == 0:
                                support_z.pos.z += 0.05
                                crane.pos.z += 0.05
                                head.pos.z += 0.05
                                i += 1
                                if i == 19:
                                        i = 0
                                        j = 1
                        if 0 < j < 8:
                                if i < 2*np.pi:
                                        support_x.pos.x = np.sin(i)
                                        crane.pos.x = np.sin(i)
                                        head.pos.x = np.sin(i)
                                        
                                        support_z.pos.z = np.cos(i)
                                        crane.pos.z = np.cos(i)
                                        head.pos.z = np.cos(i)
                                        
                                        crane.pos.y += 0.01
                                        head.pos.y += 0.01
                                        
                                        i = i + 0.05*np.pi
                                if i > 2*np.pi-0.01:
                                        i = 0
                                        j += 1
                                        
                        if j == 8:
                                j = 0
                                i = 0
                                head.make_trail = False
                                canprint = False 
                                there_is_object = True
                
                if figurechoice == 2: #Ball
                        if j < 2:
                                j_fun = np.sqrt(1-(j-1)**2)
                                if i < 2*np.pi:
                                        support_x.pos.x = np.sin(i) * j_fun
                                        crane.pos.x = np.sin(i) * j_fun
                                        head.pos.x = np.sin(i) * j_fun
                                        
                                        support_z.pos.z = np.cos(i) * j_fun
                                        crane.pos.z = np.cos(i) * j_fun
                                        head.pos.z = np.cos(i) * j_fun
                                        i = i + 0.05*np.pi
                                if i > 2*np.pi-0.01:
                                        i = 0
                                        crane.pos.y += 0.1
                                        head.pos.y += 0.1
                                        j += 0.1
                                        
                                        print(j)
                        if j > 1.905:
                                j = 0
                                i = 0
                                head.make_trail = False
                                canprint = False 
                                there_is_object = True  

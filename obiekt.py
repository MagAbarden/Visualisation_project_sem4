from vpython import *
import numpy as np

#Simulation captions
scene.caption = """Right button drag or Ctrl-drag to rotate "camera" to view scene.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
    On a two-button mouse, middle is left + right.
Shift-drag to pan left/right and up/down.

Make horizontal movement with arrow keys
Make vertical movement with "w" and "s"
"""
text(pos=vec(0, 0, 6), text='NORTH', align='center', color=color.white, up=vec(0,0,1), axis=vector(-1,0,0))

#Printer support visualisation
main_plane = box(pos=vec(0, 0, 0), length=10, height=0.1, width=10, color=color.white)

sw_support = box(pos=vec(-4.9, 2.5, -4.9), length=0.2, height=5, width=0.2, color=color.orange)
se_support = box(pos=vec(4.9, 2.5, -4.9), length=0.2, height=5, width=0.2, color=color.orange)
nw_support = box(pos=vec(-4.9, 2.5, 4.9), length=0.2, height=5, width=0.2, color=color.orange)
ne_support = box(pos=vec(4.9, 2.5, 4.9), length=0.2, height=5, width=0.2, color=color.orange)

n_support = box(pos=vec(4.9, 5, 0), length=0.2, height=0.2, width=10, color=color.orange)
s_support = box(pos=vec(-4.9, 5, 0), length=0.2, height=0.2, width=10, color=color.orange)
w_support = box(pos=vec(0, 5, 4.9), length=10, height=0.2, width=0.2, color=color.orange)
e_support = box(pos=vec(0, 5, -4.9), length=10, height=0.2, width=0.2, color=color.orange)

#Printer moving elements visualisation
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
        if evt.text == 'red':
                head.trail_color=color.red
        elif evt.text == 'green':
                head.trail_color=color.green
        elif evt.text == 'blue':
                head.trail_color=color.blue

customprint = button (bind = printfun, text = "Start printing")

clearprint = button (bind = clearfun, text = "Clear objects")

redbutton = radio(bind=colorfun, text='red', name='colors', checked=True)
greenbutton = radio(bind=colorfun, text='green', name='colors')
bluebutton = radio(bind=colorfun, text='blue', name='colors')

#Main loop
while True:
        rate(30)
        
        #Printer controls
        key = keysdown()
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
                if head.pos.y >= 0.1:
                        crane.pos.y += -0.1
                        head.pos.y += -0.1
        if 'q' in key:
                break

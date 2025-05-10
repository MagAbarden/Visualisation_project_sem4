from vpython import *
import numpy as np

#OPIS SYMULACJI
scene.caption = """Right button drag or Ctrl-drag to rotate "camera" to view scene.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
    On a two-button mouse, middle is left + right.
Shift-drag to pan left/right and up/down.

Make horizontal movement with arrow keys
Make vertical movement with "w" and "s"
"""
text(pos=vec(0, 0, 6), text='NORTH', align='center', color=color.white, up=vec(0,0,1), axis=vector(-1,0,0))

#STAŁE ELEMENTY DRUKARKI
main_plane = box(pos=vec(0, 0, 0), length=10, height=0.1, width=10, color=color.white)

sw_support = box(pos=vec(-4.9, 2.5, -4.9), length=0.2, height=5, width=0.2, color=color.orange)
se_support = box(pos=vec(4.9, 2.5, -4.9), length=0.2, height=5, width=0.2, color=color.orange)
nw_support = box(pos=vec(-4.9, 2.5, 4.9), length=0.2, height=5, width=0.2, color=color.orange)
ne_support = box(pos=vec(4.9, 2.5, 4.9), length=0.2, height=5, width=0.2, color=color.orange)

n_support = box(pos=vec(4.9, 5, 0), length=0.2, height=0.2, width=10, color=color.orange)
s_support = box(pos=vec(-4.9, 5, 0), length=0.2, height=0.2, width=10, color=color.orange)
w_support = box(pos=vec(0, 5, 4.9), length=10, height=0.2, width=0.2, color=color.orange)
e_support = box(pos=vec(0, 5, -4.9), length=10, height=0.2, width=0.2, color=color.orange)

#RUSZAJĄCE ELEMENTY DRUKARKI 
support_z = box(pos=vec(0, 5, 0), length=9.6, height=0.2, width=0.2, color=color.blue)
support_x = box(pos=vec(0, 5, 0), length=0.2, height=0.2, width=9.6, color=color.blue)

crane = box(pos=vec(0, 5.2, 0), length=0.2, height=5, width=0.2, color=color.magenta)
head = cone(pos=vec(0, 2.7, 0), axis=vec(0, -0.2, 0), radius=0.1, color=color.magenta)

#TESTOWE PIERDOŁY
#def changecords():
#    support_z.pos = support_z.pos + vec(1, 1, 1)
#change_cords = button(bind=changecords, text='change', background=color.blue)


#GŁÓWNA PĘTLA
while True:
        rate(30)
        
        #STEROWANIE DRUKARKĄ
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
                if head.pos.y > 0.3:
                        crane.pos.y += -0.1
                        head.pos.y += -0.1
        if 'q' in key:
                break
print('Done with loop')

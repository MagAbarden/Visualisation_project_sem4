from vpython import *
import numpy as np
main = canvas(width=1280, height=720, background=color.white*0.5, align = 'left')

canprint = False #Check if you can start printing figures
ifcenter = False #Check for alignment of the printer head
figurechoice = 0 #Check which figure

i = 0
j = 0
go_value = 0.1

main.caption = """Right button drag or Ctrl-drag to rotate "camera" to view scene.
To zoom, drag with middle button or Alt/Opti`on depressed, or use scroll wheel.
    On a two-button mouse, middle is left + right.
Shift-drag to pan left/right and up/down.

Make horizontal movement with arrow keys
Make vertical movement with "w" and "s"
"""
text(pos=vec(0, 0, 6), text='NORTH', align='ifcenter', color=color.white, up=vec(0,0,1), axis=vector(-1,0,0))

#PARAMETERS FOR 3D PRINTER DETAILS
#-----------------------------------------------------------------------------------
#3D printer plate parameters
plate_thickness  = 0.2
plate_width = 10
plate_lenght = 10
#3D printer vertical support beams parameters
vert_supp_thickness = 0.2
vert_supp_height = 10
#3D printer horizontal support beams parameters
hor_supp_thickness = 0.2
hor_supp_lenght = 10.4
#3D printer head parameters
head_height = 1
head_width = 1
head_length = 2
#----------------------------------------------------------------------------------
# PRINTER MODELS OF DETAILS
#3D printer base plate 
printer_plate = box(pos=vector(0,0,0), size = vector(plate_lenght,plate_thickness,plate_width), texture=textures.rock)
#3D printer vertical beams  
printer_vert_supp_beamR1 = box(pos=vector(5.1,4.9,.2), size = vector(vert_supp_thickness,vert_supp_height,vert_supp_thickness), color = color.red)
printer_vert_supp_beamR2 = box(pos=vector(5.1,4.9,-.2), size = vector(vert_supp_thickness,vert_supp_height,vert_supp_thickness), color = color.red)
printer_vert_supp_beamL1 = box(pos=vector(-5.1,4.9,.2), size = vector(vert_supp_thickness,vert_supp_height,vert_supp_thickness), color = color.red)
printer_vert_supp_beamL2 = box(pos=vector(-5.1,4.9,-.2), size = vector(vert_supp_thickness,vert_supp_height,vert_supp_thickness), color = color.red)
#3D printer horizontal beams 
printer_hor_supp_beam1 = box(pos=vector(0,.4,0), size = vector(hor_supp_lenght,hor_supp_thickness,hor_supp_thickness), color = color.blue)
#3D printer head 
printer_head = box(pos=vector(0,0.8,0), size = vector(head_length,head_height,head_width), color = color.orange)
printer_extruder = cone(pos=vector(0,0.3,0), axis=vector(0,-0.2,0), radius = 0.1, color = color.cyan)
printer_extruder_fantom = box(pos=vector(0,0.15,0), size =vector(0.01, 0.01, 0.01), color = color.cyan, make_trail=False, trail_radius = 0.1)


#3D custom print function
def printfun():
        if customprint.text == 'Start printing':
                if printer_extruder.pos.y <= 0.3:
                        printer_extruder_fantom.make_trail = True
                        customprint.text = "Stop printing"
        else:
                printer_extruder_fantom.make_trail = False
                customprint.text = "Start printing"
#delete the object                
def clearfun():
        if customprint.text == 'Start printing':
                printer_extruder_fantom.clear_trail()
#choose the color of printing 
def colorfun(evt):
        if evt.text == 'Red':
                printer_extruder_fantom.trail_color=color.red
        elif evt.text == 'Green':
                printer_extruder_fantom.trail_color=color.green
        elif evt.text == 'Blue':
                printer_extruder_fantom.trail_color=color.blue

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

# Main loop
while True:
        rate(30)
        key = keysdown()
        if 'up' in key:
                if printer_hor_supp_beam1.pos.y <= 9.7:
                        printer_hor_supp_beam1.pos.y += 0.1
                        printer_head.pos.y += 0.1
                        printer_extruder.pos.y += 0.1
                        printer_extruder_fantom.pos.y += 0.1       
        elif 'down' in key:
                if printer_hor_supp_beam1.pos.y >= 0.45:
                        printer_hor_supp_beam1.pos.y += -0.1
                        printer_head.pos.y -= 0.1
                        printer_extruder.pos.y -= 0.1
                        printer_extruder_fantom.pos.y -= 0.1  
        if 'a' in key:
                if printer_head.pos.x <= 4:
                        printer_head.pos.x +=0.1
                        printer_extruder.pos.x += 0.1
                        printer_extruder_fantom.pos.x += 0.1  
        elif 'd' in key:
                if printer_head.pos.x >= -4:
                        printer_head.pos.x -=0.1
                        printer_extruder.pos.x -= 0.1
                        printer_extruder_fantom.pos.x -= 0.1  
        if 'w' in key:
                if printer_vert_supp_beamR1.pos.z <= 4.8:
                        printer_vert_supp_beamR1.pos.z += 0.1
                        printer_vert_supp_beamR2.pos.z += 0.1
                        printer_vert_supp_beamL1.pos.z += 0.1
                        printer_vert_supp_beamL2.pos.z += 0.1
                        printer_hor_supp_beam1.pos.z += 0.1
                        printer_head.pos.z += 0.1
                        printer_extruder.pos.z += 0.1 
                        printer_extruder_fantom.pos.z += 0.1 
        elif 's' in key:
                if printer_vert_supp_beamR2.pos.z >= -4.8:
                        printer_vert_supp_beamR1.pos.z -= 0.1
                        printer_vert_supp_beamR2.pos.z -= 0.1
                        printer_vert_supp_beamL1.pos.z -= 0.1
                        printer_vert_supp_beamL2.pos.z -= 0.1
                        printer_hor_supp_beam1.pos.z -= 0.1
                        printer_head.pos.z -= 0.1
                        printer_extruder.pos.z -= 0.1
                        printer_extruder_fantom.pos.z -= 0.1 
        #Centering printer head
        if ifcenter == True:
                if printer_extruder.pos.y > 0.2:
                        printer_hor_supp_beam1.pos.y -= 0.05
                        printer_head.pos.y -= 0.05
                        printer_extruder.pos.y -= 0.05
                        printer_extruder_fantom.pos.y -= 0.05
                if printer_extruder.pos.z > 0:
                        printer_vert_supp_beamR1.pos.z -= 0.05
                        printer_vert_supp_beamR2.pos.z -= 0.05
                        printer_vert_supp_beamL1.pos.z -= 0.05
                        printer_vert_supp_beamL2.pos.z -= 0.05
                        printer_hor_supp_beam1.pos.z -= 0.05
                        printer_head.pos.z -= 0.05
                        printer_extruder.pos.z -= 0.05
                        printer_extruder_fantom.pos.z -= 0.05
                elif printer_extruder.pos.z < 0:
                        printer_vert_supp_beamR1.pos.z += 0.05
                        printer_vert_supp_beamR2.pos.z += 0.05
                        printer_vert_supp_beamL1.pos.z += 0.05
                        printer_vert_supp_beamL2.pos.z += 0.05
                        printer_hor_supp_beam1.pos.z += 0.05
                        printer_head.pos.z += 0.05
                        printer_extruder.pos.z += 0.05
                        printer_extruder_fantom.pos.z += 0.05
                if printer_extruder.pos.x > 0:
                        printer_head.pos.x -= 0.05
                        printer_extruder.pos.x -= 0.05
                        printer_extruder_fantom.pos.x -= 0.05
                elif printer_extruder.pos.x < 0:
                        printer_head.pos.x += 0.05
                        printer_extruder.pos.x += 0.05
                        printer_extruder_fantom.pos.x += 0.05
                if -0.1 < printer_extruder.pos.x < 0.1 and -0.1 < printer_extruder.pos.z < 0.1 and printer_extruder.pos.y < 0.3:
                        canprint = True
                        ifcenter = False
                        printer_extruder_fantom.make_trail = True

        #Start printing
        if canprint == True:
                if figurechoice == 0: #Rectangle
                        if j < 16 :
                                if i < 16:
                                        printer_head.pos.x += go_value
                                        printer_extruder.pos.x += go_value
                                        printer_extruder_fantom.pos.x += go_value
                                        i += 1
                                if i == 16:
                                        printer_vert_supp_beamR1.pos.z += 0.1
                                        printer_vert_supp_beamR2.pos.z += 0.1
                                        printer_vert_supp_beamL1.pos.z += 0.1
                                        printer_vert_supp_beamL2.pos.z += 0.1
                                        printer_hor_supp_beam1.pos.z += 0.1
                                        printer_head.pos.z += 0.1
                                        printer_extruder.pos.z += 0.1
                                        printer_extruder_fantom.pos.z += 0.1  
                                        i = 0
                                        go_value = -go_value
                                        j += 1
                        if 15 < j < 24:
                                if i < 16:
                                        printer_head.pos.x += 0.1
                                        printer_extruder.pos.x += 0.1
                                        printer_extruder_fantom.pos.x += 0.1
                                elif 15 < i < 32:
                                        printer_vert_supp_beamR1.pos.z -= 0.1
                                        printer_vert_supp_beamR2.pos.z -= 0.1
                                        printer_vert_supp_beamL1.pos.z -= 0.1
                                        printer_vert_supp_beamL2.pos.z -= 0.1
                                        printer_hor_supp_beam1.pos.z -= 0.1
                                        printer_head.pos.z -= 0.1
                                        printer_extruder.pos.z -= 0.1
                                        printer_extruder_fantom.pos.z -= 0.1  
                                elif 31 < i < 48:
                                        printer_head.pos.x -= 0.1
                                        printer_extruder.pos.x -= 0.1
                                        printer_extruder_fantom.pos.x -= 0.1
                                elif 47 < i < 64:
                                        printer_vert_supp_beamR1.pos.z += 0.1
                                        printer_vert_supp_beamR2.pos.z += 0.1
                                        printer_vert_supp_beamL1.pos.z += 0.1
                                        printer_vert_supp_beamL2.pos.z += 0.1
                                        printer_hor_supp_beam1.pos.z += 0.1
                                        printer_head.pos.z += 0.1
                                        printer_extruder.pos.z += 0.1
                                        printer_extruder_fantom.pos.z += 0.1         
                                i += 1
                                if i == 64:
                                        printer_hor_supp_beam1.pos.y += 0.2
                                        printer_head.pos.y += 0.2
                                        printer_extruder.pos.y += 0.2
                                        printer_extruder_fantom.pos.y += 0.2       
                                        i = 0
                                        j += 1
                        if 23 < j < 40:
                                if i < 16:
                                        printer_head.pos.x += go_value
                                        printer_extruder.pos.x += go_value
                                        printer_extruder_fantom.pos.x += go_value 
                                        i += 1
                                if i == 16:
                                        printer_vert_supp_beamR1.pos.z -= 0.1
                                        printer_vert_supp_beamR2.pos.z -= 0.1
                                        printer_vert_supp_beamL1.pos.z -= 0.1
                                        printer_vert_supp_beamL2.pos.z -= 0.1
                                        printer_hor_supp_beam1.pos.z -= 0.1
                                        printer_head.pos.z -= 0.1
                                        printer_extruder.pos.z -= 0.1
                                        printer_extruder_fantom.pos.z -= 0.1
                                        i = 0
                                        go_value = -go_value
                                        j += 1
                        if j == 40:
                               printer_extruder_fantom.make_trail = False
                               canprint = False
                               i = 0
                               j = 0

                if figurechoice == 1: #Spring
                                if j == 0:
                                        printer_vert_supp_beamR1.pos.z += 0.05 
                                        printer_vert_supp_beamR2.pos.z += 0.05 
                                        printer_vert_supp_beamL1.pos.z += 0.05 
                                        printer_vert_supp_beamL2.pos.z += 0.05 
                                        printer_hor_supp_beam1.pos.z += 0.05 
                                        printer_head.pos.z += 0.05 
                                        printer_extruder.pos.z += 0.05  
                                        printer_extruder_fantom.pos.z += 0.05 
                                        i += 1
                                        if i == 19:
                                                i = 0
                                                j = 1
                                if 0 < j < 8:
                                        if i < 2*np.pi:  # = np.cos(i)
                                                printer_head.pos.x = np.sin(i)
                                                printer_extruder.pos.x = np.sin(i)
                                                printer_extruder_fantom.pos.x = np.sin(i) 
                                                
                                                printer_vert_supp_beamR1.pos.z = np.cos(i)-0.4
                                                printer_vert_supp_beamR2.pos.z = np.cos(i)
                                                printer_vert_supp_beamL1.pos.z = np.cos(i)-0.4
                                                printer_vert_supp_beamL2.pos.z = np.cos(i)
                                                printer_hor_supp_beam1.pos.z = np.cos(i)-0.2
                                                printer_head.pos.z = np.cos(i)-0.2
                                                printer_extruder.pos.z = np.cos(i)
                                                printer_extruder_fantom.pos.z = np.cos(i)
                                                
                                                printer_hor_supp_beam1.pos.y += 0.01
                                                printer_head.pos.y += 0.01
                                                printer_extruder.pos.y += 0.01
                                                printer_extruder_fantom.pos.y += 0.01
                                                
                                                i = i + 0.05*np.pi
                                        if i > 2*np.pi-0.01:
                                                i = 0
                                                j += 1
                                                
                                if j == 8:
                                        j = 0
                                        i = 0
                                        printer_extruder_fantom.make_trail = False
                                        canprint = False 
                                        there_is_object = True
                if figurechoice == 2: #Ball
                        if j < 2:
                                j_fun = np.sqrt(1-(j-1)**2)  # = np.cos(i) * j_fun
                                if i < 2*np.pi:
                                        printer_head.pos.x = np.sin(i) * j_fun
                                        printer_extruder.pos.x = np.sin(i) * j_fun
                                        printer_extruder_fantom.pos.x = np.sin(i) * j_fun
                                        
                                        printer_vert_supp_beamR1.pos.z = np.cos(i) * j_fun -0.2
                                        printer_vert_supp_beamR2.pos.z = np.cos(i) * j_fun +0.2
                                        printer_vert_supp_beamL1.pos.z = np.cos(i) * j_fun -0.2
                                        printer_vert_supp_beamL2.pos.z = np.cos(i) * j_fun +0.2
                                        printer_hor_supp_beam1.pos.z = np.cos(i) * j_fun
                                        printer_head.pos.z = np.cos(i) * j_fun
                                        printer_extruder.pos.z = np.cos(i) * j_fun
                                        printer_extruder_fantom.pos.z = np.cos(i) * j_fun
                                        i = i + 0.05*np.pi
                                if i > 2*np.pi-0.01:
                                        i = 0
                                        printer_hor_supp_beam1.pos.y += 0.1
                                        printer_head.pos.y += 0.1
                                        printer_extruder.pos.y += 0.1
                                        printer_extruder_fantom.pos.y += 0.1   
                                        j += 0.1
                                        
                                        #print(j)
                        if j > 1.905:
                                j = 0
                                i = 0
                                printer_extruder_fantom.make_trail = False
                                canprint = False 
                                there_is_object = True  
                
        if 'esc' in key:
                break
        
                  

        

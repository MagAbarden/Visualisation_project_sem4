from vpython import *
import numpy as np
canvas(width=1280, height=720, background=color.white)
#PARAMETERS FOR 3D PRINTER DETAILS

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

# Manual operating of 3D printer
while True:
        rate(30)
        key = keysdown()
        if 'up' in key:
                if printer_hor_supp_beam1.pos.y <= 9.7:
                        printer_hor_supp_beam1.pos.y += 0.1
                        printer_head.pos.y += 0.1
                        printer_extruder.pos.y += 0.1       
        elif 'down' in key:
                if printer_hor_supp_beam1.pos.y >= 0.45:
                        printer_hor_supp_beam1.pos.y += -0.1
                        printer_head.pos.y -= 0.1
                        printer_extruder.pos.y -= 0.1  
        if 'a' in key:
                if printer_head.pos.x <= 4:
                        printer_head.pos.x +=0.1
                        printer_extruder.pos.x += 0.1  
        elif 'd' in key:
                if printer_head.pos.x >= -4:
                        printer_head.pos.x -=0.1
                        printer_extruder.pos.x -= 0.1  
        if 'w' in key:
                if printer_vert_supp_beamR1.pos.z <= 4.8:
                        printer_vert_supp_beamR1.pos.z += 0.1
                        printer_vert_supp_beamR2.pos.z += 0.1
                        printer_vert_supp_beamL1.pos.z += 0.1
                        printer_vert_supp_beamL2.pos.z += 0.1
                        printer_hor_supp_beam1.pos.z += 0.1
                        printer_head.pos.z += 0.1
                        printer_extruder.pos.z += 0.1  
        elif 's' in key:
                if printer_vert_supp_beamR2.pos.z >= -4.8:
                        printer_vert_supp_beamR1.pos.z -= 0.1
                        printer_vert_supp_beamR2.pos.z -= 0.1
                        printer_vert_supp_beamL1.pos.z -= 0.1
                        printer_vert_supp_beamL2.pos.z -= 0.1
                        printer_hor_supp_beam1.pos.z -= 0.1
                        printer_head.pos.z -= 0.1
                        printer_extruder.pos.z -= 0.1  
        elif 'q' in key:
                break

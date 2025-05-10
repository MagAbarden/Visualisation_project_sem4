import vpython as vp
from time import *
plate_thickness = .1 
plate_sideX = 10
plate_sideY = 2
plate_sideZ = 10
pingRadius = .5
base = vp.box(pos = vp.vector(0,-plate_sideY/2,0), color = vp.color.white, length = plate_sideX, height = plate_thickness, width = plate_sideZ)
#roof = vp.box(pos = vp.vector(0,plate_sideY/2,0), color = vp.color.white, length = plate_sideX, height = plate_thickness, width = plate_sideZ)
wall_right = vp.box(pos = vp.vector(plate_sideX/2,0,0), color = vp.color.white, length = plate_thickness, height = plate_sideY, width = plate_sideZ)
wall_left = vp.box(pos = vp.vector(-plate_sideX/2,0,0), color = vp.color.white, length = plate_thickness, height = plate_sideY, width = plate_sideZ)
wall_back = vp.box(pos = vp.vector(0,0,-plate_sideZ/2), color = vp.color.white, length = plate_sideX, height = plate_sideY, width = plate_thickness)
wall_front = vp.box(pos = vp.vector(0,0,plate_sideZ/2), color = vp.color.white, length = plate_sideX, height = plate_sideY, width = plate_thickness)
ping_pong_ball = vp.sphere(radius = pingRadius, color = vp.color.red)
delta_ping = .01
ping = 0
while True:
    vp.rate(120)
    ping = ping+ delta_ping
    if(ping > (plate_sideX/2)-pingRadius-plate_thickness or ping <-(plate_sideX/2)+pingRadius+plate_thickness):
        delta_ping = delta_ping*(-1)
    ping_pong_ball.pos = vp.vector(ping,0,0)
    pass

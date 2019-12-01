import mcpi.minecraft as minecraft
import time
import sys
import keyboard
import random
import mcpi.block as block
mc = minecraft.Minecraft.create()
#Площадка
mc.setBlocks(0,180,0,50,180,50,2)
#Лакиблок
x = random.randint(0,50)
z = random.randint(0,50)
mc.setBlock(x,184,z,41)
#Уничтожение блока
while True:
    pos = mc.player.getTilePos()
    if round(pos.x) == x and round (pos.z)==z:
        mc.setBlock(x,184,z,0)
    


# File to test minecraft server commands
from minecraftstuff import MinecraftTurtle
from mcpi.minecraft import Minecraft
from mcpi import block
import random

# server connection test
mc = Minecraft.create("localhost", 4711)
myId = mc.getPlayerEntityId("MinecraftMoleMan")
myPos = mc.entity.getPos(myId)

"""
turtle test code
"""
# creates turtle
turtle = MinecraftTurtle(mc, myPos)

# draws square
for i in range(4):
    turtle.forward(5)
    turtle.right(90)

#changes pen block
#turtle.penblock(block.DIRT.id)

"""
Custome method to create house
"""
def house_creator():
    # player location
    x, y, z = myPos.x, myPos.y, myPos.z

    # create walls in front of and behind player
    create_wall(x, y, z)

#helper method to create walls
def create_wall(x, y, z):
    xLow, xHigh = int(x)-5, int(x)+5
    yLow, yHigh = int(y), int(y)+10
    zLow, zHigh = int(z)-5, int(z)+5

    #torch for light
    mc.setBlock(x, y, z, block.TORCH.id)

    #traps player inside room
    for i in range(xLow, xHigh+1):
        for j in range(yLow, yHigh+1):
            for k in range(zLow, zHigh+1):
                if i == xLow or i ==xHigh or j == yLow or j ==yHigh or k == zLow or k == zHigh:
                    mc.setBlock(i, j, k, block.DIRT.id)
house_creator()




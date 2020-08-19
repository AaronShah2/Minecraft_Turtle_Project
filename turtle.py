from minecraftstuff import MinecraftTurtle
from mcpi.minecraft import Minecraft
from usernames import USERNAME
# test code to be deleted later
mc = Minecraft.create("localhost", 4711)
myId = mc.getPlayerEntityId(USERNAME)
myPos = mc.entity.getPos(myId)
turtle = MinecraftTurtle(mc, myPos)

# helper methods
def line(turtle, x, y, z, units):
    turtle.setposition(x, y, z)
    turtle.forward(units)

def a(turtle, x, y, z):
    # two sideways lines
    turtle.right(90)
    line(turtle, x, y+2, z, 4)
    line(turtle, x , y+4, z, 4)
    turtle.left(90)

    # legs
    turtle.up(90)
    line(turtle, x, y, z + 4, 4)
    line(turtle, x, y, z, 4)
    turtle.down(90)

def r(turtle, x, y, z):
    # diagonal leg
    turtle.left(90)
    turtle.up(45)
    line(turtle, x, y, z+3, 3)
    turtle.right(90)
    turtle.down(45)

    # two sideways lines
    turtle.right(90)
    line(turtle, x, y+4, z, 3)
    line(turtle, x, y+2, z, 3)
    turtle.left(90)

    # two upwards lines
    turtle.up(90)
    line(turtle, x, y, z, 4)
    line(turtle, x, y+2, z+3, 2)
    turtle.down(90)

def o(turtle, x, y, z):
    # two sideways lines
    turtle.right(90)
    line(turtle, x, y + 4, z, 4)
    line(turtle, x, y, z, 4)
    turtle.left(90)

    # two upright legs
    turtle.up(90)
    line(turtle, x, y, z + 4, 4)
    line(turtle, x, y, z, 4)
    turtle.down(90)


def n(turtle, x, y, z):
    # diagonal leg
    turtle.left(90)
    turtle.up(45)
    line(turtle, x, y, z + 4, 4)
    turtle.right(90)
    turtle.down(45)

    # legs
    turtle.up(90)
    line(turtle, x, y, z + 4, 4)
    line(turtle, x, y, z, 4)
    turtle.down(90)

# Turtle  Driver
if __name__ == "__main__":
    # location coordinate trackers
    turtle = MinecraftTurtle(mc, myPos)
    x, y, z = myPos.x, myPos.y, myPos.z
    # writes my name
    a(turtle, x + 5, y, z)
    a(turtle, x + 5, y, z+6)
    r(turtle, x + 5, y, z+12)
    o(turtle, x + 5, y, z+18)
    n(turtle, x + 5, y, z+24)
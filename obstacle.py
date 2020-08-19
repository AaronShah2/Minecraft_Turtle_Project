from mcpi.minecraft import Minecraft
from mcpi import block



# Connects to Server
MC = Minecraft.create("localhost", 4711)

# creates starting area
def start_area(mc, x, y, z, material):
    # creates starting platform for player to sit on
    mc.setBlocks(x-3, y - 2, z-3, x+3, y-2, z+3, material)

    # creates torches to use as light source
    mc.setBlock(x-3, y - 1, z-3, block.TORCH.id)
    mc.setBlock(x+3, y - 1, z+3, block.TORCH.id)
    mc.setBlock(x - 3, y - 1, z + 3, block.TORCH.id)
    mc.setBlock(x + 3, y - 1, z-3, block.TORCH.id)

    # Plops player at the beginning of the obstacle course
    mc.player.setPos(x,y,z)

# creates checkpoint where the player can respawn
def checkpoint(mc, x, y, z, material):
    # sets up line to indiciate checkpoint
    mc.setBlocks(x, y - 2, z - 2, x, y - 2, z + 2, material)

# builds first obstacle
def obstacle_one(mc, x, y, z, material):
    # starting area
    mc.setBlocks(x, y-4, z-2, x+3, y-2, z+2, material)
    mc.setBlock(x+3, y-1, z-2,  block.TORCH.id)
    mc.setBlock(x + 3, y - 1, z + 2, block.TORCH.id)
    # gap in the middle
    mc.setBlocks(x+1, y-6, z-3, x+6, y-4, z+3, material)

    # stairs to get back to starting area
    mc.setBlocks(x+1, y-3, z-3, x+1, y-2, z+3, material)
    mc.setBlocks(x + 2, y - 3, z - 3, x + 2, y - 3, z + 3, material)
    # goal
    mc.setBlocks(x+7, y-4, z-2, x+10, y-2, z+2, material)
    mc.setBlock(x + 7, y - 1, z - 2, block.TORCH.id)
    mc.setBlock(x + 7, y - 1, z + 2, block.TORCH.id)

# builds second obstacle
def obstacle_two(mc, x, y, z, material):
    # starting area
    mc.setBlocks(x, y-4, z-2, x+3, y-2, z+2, material)
    mc.setBlock(x+3, y-1, z-2,  block.TORCH.id)
    mc.setBlock(x + 3, y - 1, z + 2, block.TORCH.id)

    # goal
    mc.setBlocks(x+7, y-4, z-2, x+10, y-2, z+2, material)
    mc.setBlock(x + 7, y - 1, z - 2, block.TORCH.id)
    mc.setBlock(x + 7, y - 1, z + 2, block.TORCH.id)

# builds second obstacle
def obstacle_three(mc, x, y, z, material):
    # starting area
    mc.setBlocks(x, y-4, z-2, x+3, y-2, z+2, material)

# moves obstacle 3
def obstacle_three_movement(mc, x0, y0, z0, x1, y1, z1, material):
    obstacle_three(mc, x0, y0, z0, block.AIR)
    obstacle_three(mc, x1, y1, z1, material)
# creates platform where the obstacle course will end
def end_area(mc, x, y, z, material):
    # creates ending areea platform for player to sit on
    mc.setBlocks(x-2, y - 2, z-2, x+2, y-2, z+2, material)

    # creates torches to use as light source
    mc.setBlock(x - 2, y - 1, z - 2, block.TORCH.id)
    mc.setBlock(x + 2, y - 1, z + 2, block.TORCH.id)
    mc.setBlock(x - 2, y - 1, z + 2, block.TORCH.id)
    mc.setBlock(x + 2, y - 1, z - 2, block.TORCH.id)



# Respawns player back to top if they have fallen more than 50 blocks
def check_if_player_fell(mc, x, y,z):
    playerPos = mc.player.getPos()
    if playerPos.y < y - 50:
        mc.player.setPos(x, y, z)

def player_reach_checkpoint(mc, checkpointBlock):
    playerPos = mc.player.getPos()
    return mc.getBlock(playerPos.x, playerPos.y - 1, playerPos.z) == checkpointBlock

# checks if player has reached the finish line
def player_finished(mc, finishLineBlock):
    playerPos = mc.player.getPos()
    return mc.getBlock(playerPos.x, playerPos.y - 1, playerPos.z) == finishLineBlock


# Obstacle Course Driver
if __name__ == "__main__":
    # location coordinate trackers
    startingPosition = {"x": 0,
                         "y": 200,
                         "z": 0}
    respawnPoint = startingPosition.copy()

    # Block ids that will be used in the obstacle course
    obstacleBlock = block.STONE.id #stone
    finishLineBlock = block.BEDROCK.id #bedrock
    checkpointBlock = block.DIRT.id # DIRT
    deleteBlock = block.AIR.id

    # Builds obstacle course
    start_area(
        MC,
        startingPosition["x"],
        startingPosition["y"],
        startingPosition["z"],
        obstacleBlock
    )

    obstacle_one(
        MC,
        startingPosition["x"]+4,
        startingPosition["y"],
        startingPosition["z"],
        obstacleBlock
    )
    checkpoint(
        MC,
        startingPosition["x"]+15,
        startingPosition["y"],
        startingPosition["z"],
        checkpointBlock
    )
    obstacle_two(
        MC,
        startingPosition["x"] + 16,
        startingPosition["y"],
        startingPosition["z"],
        obstacleBlock
    )
    checkpoint(
        MC,
        startingPosition["x"] + 27,
        startingPosition["y"],
        startingPosition["z"],
        checkpointBlock
    )

    obstacle_three(
        MC,
        startingPosition["x"] + 28,
        startingPosition["y"],
        startingPosition["z"],
        obstacleBlock
    )
    # keeps track of starting & ending positions of obstacle 3
    obstacleThreeCurrent = {
        "x": startingPosition["x"] + 28,
        "y": startingPosition["y"],
        "z": startingPosition["z"],
    }
    obstacleThreeStart = startingPosition["x"] + 28
    obstacleThreeEnd = startingPosition["x"] + 34
    obstacleThreeForward = True
    end_area(
        MC,
        startingPosition["x"] + 40,
        startingPosition["y"],
        startingPosition["z"],
        finishLineBlock
    )

    # Post to chat that the obstacle couse has started
    MC.postToChat("The Obstacle course has begun!")

    isFinished = False
    while not isFinished:
        check_if_player_fell(
            MC,
            respawnPoint["x"],
            respawnPoint["y"],
            respawnPoint["z"]
        )

        #checks if player has passed checkpoint
        if player_reach_checkpoint(MC, checkpointBlock):
            if int(respawnPoint["x"]) - int(MC.player.getPos().x) >=1 or int(respawnPoint["x"]) - int(MC.player.getPos().x) <= -1:
                MC.postToChat("You reached a checkpoint!")
                respawnPoint["x"], respawnPoint["y"], respawnPoint["z"] = MC.player.getPos().x, MC.player.getPos().y, MC.player.getPos().z

        # allows obstacle 3 to move
        if obstacleThreeCurrent["x"] <= obstacleThreeStart:
            obstacleThreeForward = True
        if obstacleThreeCurrent["x"] >= obstacleThreeEnd:
            obstacleThreeForward = False
        if obstacleThreeForward:
            obstacle_three_movement(
                MC,
                obstacleThreeCurrent["x"],
                obstacleThreeCurrent["y"],
                obstacleThreeCurrent["z"],
                obstacleThreeCurrent["x"] + 1,
                obstacleThreeCurrent["y"],
                obstacleThreeCurrent["z"],
                obstacleBlock
            )
            obstacleThreeCurrent["x"] += 1
        else:
            obstacle_three_movement(
                MC,
                obstacleThreeCurrent["x"],
                obstacleThreeCurrent["y"],
                obstacleThreeCurrent["z"],
                obstacleThreeCurrent["x"]-1,
                obstacleThreeCurrent["y"],
                obstacleThreeCurrent["z"],
                obstacleBlock
            )
            obstacleThreeCurrent["x"] -= 1

        # checks if MC is standing on Finish line blocks
        isFinished = player_finished(MC, finishLineBlock)
    # Tells player they have finished playing the obstacle course
    MC.postToChat("Hooray! You beat the obstacle course!")

    # Deletes everything
    start_area(
        MC,
        startingPosition["x"],
        startingPosition["y"],
        startingPosition["z"],
        deleteBlock
    )

    obstacle_one(
        MC,
        startingPosition["x"] + 4,
        startingPosition["y"],
        startingPosition["z"],
        deleteBlock
    )
    checkpoint(
        MC,
        startingPosition["x"] + 15,
        startingPosition["y"],
        startingPosition["z"],
        deleteBlock
    )
    obstacle_two(
        MC,
        startingPosition["x"] + 16,
        startingPosition["y"],
        startingPosition["z"],
        deleteBlock
    )
    checkpoint(
        MC,
        startingPosition["x"] + 27,
        startingPosition["y"],
        startingPosition["z"],
        deleteBlock
    )

    obstacle_three(
        MC,
        obstacleThreeCurrent["x"],
        obstacleThreeCurrent["y"],
        obstacleThreeCurrent["z"],
        deleteBlock
    )
    end_area(
        MC,
        startingPosition["x"] + 40,
        startingPosition["y"],
        startingPosition["z"],
        deleteBlock
    )


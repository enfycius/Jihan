from mcpi.minecraft import Minecraft

mc = Minecraft.create()

mc.postToChat("Hello, Minecraft World")

pos = mc.player.getTilePos()

mc.postToChat(str(pos.x) + " " + str(pos.y) + " " + str(pos.z))

# print("Hello " + "World")

# print("Hello " + "World")

# print("Hello" + " " + "World")

def make_step(a):
    for i in range(0, a):
        mc.setBlock(-24 + i, -10 + i, -3 + i, 21)


make_step(10)
    





# 실수: 소수점이 있는 숫자


from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
PLATFORM_WIDTH = 16

def input(key):
    if key == "escape":
        quit()


class Block(Button):
    def __init__(self, texture = "white_cube", **kwargs):
        super().__init__(
            parent = scene,
            model = Mesh(
                vertices = [
                    [0, 0, 0], 
                    [1, 0, 0], 
                    [1, 0, 1], 
                    [0, 0, 1],
                    [0, 1, 0], 
                    [1, 1, 0], 
                    [1, 1, 1], 
                    [0, 1, 1],
                ],
                triangles = [
                    [3, 2, 1, 0],
                    [0, 1, 5, 4],
                    [1, 2, 6, 5],
                    [2, 3, 7, 6],
                    [3, 0, 4, 7],
                    [4, 5, 6, 7],
                ],
                normals = [
                    [-1, -1, -1], 
                    [1, -1, -1], 
                    [1, -1, 1], 
                    [-1, -1, 1],
                    [-1, 1, -1], 
                    [1, 1, -1], 
                    [1, 1, 1], 
                    [-1, 1, 1],
                ],
                uvs = [
                    [0, 0], [1, 0], [1, 1], [0, 1],
                    [0, 0], [1, 0], [1, 1], [0, 1],
                ],
            ),
            collider = "box",
            texture = texture,
            **kwargs,
        )
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                destroy(self)
            elif key == "right mouse down":
                self.__class__(
                    position = self.position + mouse.normal,
                )


class Grass(Block):
    def __init__(self, **kwargs):
        super().__init__(
            color = color.green,
            texture = "grass",
            **kwargs,
        )
        

class Dirt(Block):
    def __init__(self, **kwargs):
        super().__init__(
            color = color.brown,
            **kwargs,
        )

app = Ursina()

player = FirstPersonController()

Sky()

for x in range(10):
    for y in range(10):
        for z in range(10):
            if y == 0:
                grass = Grass(position = (x, y, z))
            else:
                dirt = Dirt(position = (x, -y, z))

app.run()
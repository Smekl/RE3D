import math

import pyglet
from pyglet.gl import *  # type: ignore

from src.model_loader import load_obj


def create_vertex_list(model):
    vertices = [coord for vertex in model.vertices for coord in vertex]
    indices = [index - 1 for face in model.faces for index in face]
    return pyglet.graphics.vertex_list_indexed(
        len(model.vertices), indices, ("v3f/static", vertices)
    )


def main(path: str):
    model = load_obj(path)
    vertex_list = create_vertex_list(model)

    window = pyglet.window.Window(800, 600, "OBJ Viewer", resizable=True)

    @window.event
    def on_draw():
        window.clear()
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect = window.width / float(window.height)
        gluPerspective(60.0, aspect, 0.1, 100.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -3.0)
        glRotatef(on_draw.angle, 0.0, 1.0, 0.0)

        glEnable(GL_DEPTH_TEST)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        vertex_list.draw(GL_TRIANGLES)
        glDisable(GL_DEPTH_TEST)

        on_draw.angle += 1

    on_draw.angle = 0.0

    pyglet.app.run()


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python obj_viewer.py path/to/model.obj")
        sys.exit(1)
    main(sys.argv[1])


import sys, random
from pyglet.gl import *
from pyglet.window import *

window = pyglet.window.Window(800,600)

scale = 1
verts = [0,90, 800,90]
vlist = pyglet.graphics.vertex_list(len(verts)/2, ('v2f', verts))

def mpFind(array):
    for i in range(0,(len(array)-3)):
        i = i*(random.randint(2, 3))
        mp1 = array[i+2]
        mp2 = array[i]
        if array[i+1] > array[i+3]:
            y1 = array[i+3]
            y2 = array[i+1]
        if array[i+1] <= array[i+3]:
            y1 = array[i+1]
            y2 = array[i+3]
        array.insert(i+2, (y1+y2)/2+random.uniform(-300*scale,300*scale))
        array.insert(i+2, (mp1+mp2)/2)

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,1,0)
    pyglet.graphics.vertex_list(len(verts)/2, ('v2f', verts)).draw(GL_LINE_STRIP)

@window.event
def on_key_press(key,modifiers):
    global vlist, scale
    if key == pyglet.window.key.SPACE:
        scale /= random.randrange(2.0, 3.0) + 0.5
        mpFind(verts)

pyglet.app.run()

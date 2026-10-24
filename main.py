import glfw
from OpenGL.GL import *

glfw.init()
w = glfw.create_window(800, 600, "Lab 1", None, None)
glfw.make_context_current(w)
print("GL", glGetString(GL_VERSION).decode(), "on", glGetString(GL_RENDERER).decode())

while not glfw.window_should_close(w):
    glClearColor(0.8, 0.2, 0.5, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glfw.swap_buffers(w)
    glfw.poll_events()
glfw.terminate()
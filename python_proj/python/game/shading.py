import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Initialize Pygame and OpenGL
pygame.init()
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
gluPerspective(45, (width / height), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Fur shader
vertex_shader = """
#version 330
layout(location = 0) in vec4 position;
uniform mat4 modelview;
void main()
{
    gl_Position = modelview * position;
}
"""

fragment_shader = """
#version 330
out vec4 FragColor;
void main()
{
    FragColor = vec4(0.5, 0.2, 0.1, 1.0);
}
"""

shader_program = glCreateProgram()
vertex_shader_object = glCreateShader(GL_VERTEX_SHADER)
glShaderSource(vertex_shader_object, vertex_shader)
glCompileShader(vertex_shader_object)
glAttachShader(shader_program, vertex_shader_object)

fragment_shader_object = glCreateShader(GL_FRAGMENT_SHADER)
glShaderSource(fragment_shader_object, fragment_shader)
glCompileShader(fragment_shader_object)
glAttachShader(shader_program, fragment_shader_object)

glLinkProgram(shader_program)
glUseProgram(shader_program)

# Fur parameters
fur_length = 0.2
fur_density = 500

# Fur vertices
fur_vertices = []
for i in range(fur_density):
    fur_vertices.extend([0.0, 0.0, 0.0])
    fur_vertices.extend([0.0, fur_length, 0.0])

fur_vertices = (GLfloat * len(fur_vertices))(*fur_vertices)
fur_vertex_buffer = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, fur_vertex_buffer)
glBufferData(GL_ARRAY_BUFFER, fur_vertices, GL_STATIC_DRAW)

# Fur VAO
fur_vao = glGenVertexArrays(1)
glBindVertexArray(fur_vao)
glEnableVertexAttribArray(0)
glBindBuffer(GL_ARRAY_BUFFER, fur_vertex_buffer)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUniformMatrix4fv(
        glGetUniformLocation(shader_program, "modelview"), 1, GL_FALSE, glGetFloatv(GL_MODELVIEW_MATRIX)
    )

    glBindVertexArray(fur_vao)
    glDrawArrays(GL_LINES, 0, fur_density * 2)
    pygame.display.flip()
    pygame.time.wait(10)

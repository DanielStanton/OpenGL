import pygame
from pygame.locals import *
import math
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = [
    (0, 0, 0),
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 1, 1),
    (0, 0, 1),
    (1, 0, 1),
    (1, 1, 1)
    ]

edges = [
    (0, 1),
    (0, 3),
    (0, 5),
    (2, 1),
    (2, 3),
    (2, 7),
    (4, 3),
    (4, 5),
    (4, 7),
    (6, 1),
    (6, 5),
    (6, 7),
    ]

faces = [
    (0, 1, 2, 3),
    (1, 6, 7, 2),
    (6, 5, 4, 7),
    (5, 0, 3, 4),
    (3, 2, 7, 4),
    (0, 1, 6, 5)
    ]

colours = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
    ]

def create_cube():
    glBegin(GL_QUADS)
    x=0
    for face in faces:
        for vertex in face:
            x+=1
            if x < 5:
                glColor3fv((0, 0, 0))
                glVertex3fv(vertices[vertex])
            elif x < 9:
                glColor3fv((0, 0, 1))
                glVertex3fv(vertices[vertex])
            elif x < 13:
                glColor3fv((0, 1, 0))
                glVertex3fv(vertices[vertex])
            elif x < 17:
                glColor3fv((0, 1, 1))
                glVertex3fv(vertices[vertex])
            elif x < 21:
                glColor3fv((1, 0, 0))
                glVertex3fv(vertices[vertex])
            elif x < 25:
                glColor3fv((1, 0, 1))
                glVertex3fv(vertices[vertex])
            #glColor3fv(colours[x])
            #glVertex3fv(vertices[vertex])
    glEnd()
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])   
    glEnd()
def cross(a, b):
    x = (a[1] * b[2]) - (a[2] * b[1])
    y = (a[2] * b[0]) - (a[0] * b[2])
    z = (a[0] * b[1]) - (a[1] * b[0])
    c = (x, y, z)
    return c
    
def main():
    pygame.init()
    DISPLAY = (800, 800)
    pygame.display.set_mode(DISPLAY, DOUBLEBUF|OPENGL)

    gluPerspective(45, DISPLAY[0]/DISPLAY[1], 0.1, 50.0)

    glTranslatef(-0.5, -0.5, -5)

    glRotatef(0, 0, 0, 0)

    pygame.mouse.set_pos(DISPLAY[0]/2, DISPLAY[1]/2)
    mouse_down = False
    pygame.mouse.set_visible(False)
    looking = (0, 0, 0)
    
    while True:
        dx, dy = pygame.mouse.get_rel()
        #mx, my = pygame.mouse.get_pos()
        
        #if (dx + mx) > DISPLAY[0]:
        #    dx = DISPLAY[0] - mx
        #elif (dx + mx) < 0:
        #    dx = 0
            
        #if (dy + my) > DISPLAY[1]:
        #    dy = DISPLAY[1] - my
        #elif (dy + my) < 0:
        #    dy = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    glTranslatef(0, 0, 1)
                if event.key == K_s:
                    glTranslatef(0, 0, -1)
                if event.key == K_a:
                    glTranslatef(1, 0, 0)
                if event.key == K_d:
                    glTranslatef(-1, 0, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        glTranslatef(0, 0, 1)
                    if event.button == 5:
                        glTranslatef(0, 0, -1)
                    if event.button == 1:
                        mouse_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_down = False
                    
        if mouse_down:
            #glRotatef(10, 0, 1, 0)
            theta = -1 * math.asin((2 * dy) / DISPLAY[1])
            beta = -1 * math.asin((2 * dx) / DISPLAY[0])
            glRotatef(theta, 1, 0, 0)
            glRotatef(beta, 0, 1, 0)
            
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        create_cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()

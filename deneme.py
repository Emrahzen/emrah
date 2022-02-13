from pygame.locals import *
import pygame,sys
from turtle import Screen, pos
pygame.init()
Screen-pygame.display.set_mode((640,360),0,32)
color=(200,155,64)
pos1=(20,20)
pos2=(150,143)
points=[]
while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONDOWN:
                points.append(event,pos)
        if len(points)>1:
            pygame.draw.lines(Screen,color,False,points,5)

        Screen.lock()
        pygame.draw.line(Screen,color,pos1,pos2)
        Screen.unlock()  
        pygame.display.update()             
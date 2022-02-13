from pygame.locals import *
import pygame

pygame.init()
Screen=pygame.display.set_mode((640,360),0,32)
color=(255,255,255)
points=[]
while True:
    print(MOUSEBUTTONDOWN)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==MOUSEBUTTONDOWN:
            points.append(event.pos)
    if len(points)>1:
        pygame.draw.lines(Screen,color,False,points,5)

    pygame.display.update()             
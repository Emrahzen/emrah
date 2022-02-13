
import pygame

Screen_widht= 600
Screen_height= 600
grid_size= 20
grid_widht=Screen_widht/grid_size
grid_height=Screen_height/grid_size

light_red=(0,170,240)
dark_red=(0,140,120)
car_color=(255,255,255)
        
def main():

    soltus=pygame.K_LEFT
    sagtus=pygame.K_RIGHT
    yukaritus=pygame.K_UP
    asagitus=pygame.K_DOWN
    
    hiz=10
    arabaResim = pygame.image.load('araba.jpg')            
    arabawidth=20
    arabaheight=50
    x=280
    y=280
    
    pygame.init()
    Screen = pygame.display.set_mode((Screen_widht,Screen_height))
    font =pygame.font.SysFont("arial",20)
    surface= pygame.Surface(Screen.get_size())
    surface= surface.convert()
    yon="YUKARI"

    while True:
        for event in pygame.event.get():
            pygame.time.Clock().tick(10000000000)
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                
        if pygame.key.get_pressed()[soltus]:
            if yon=="YUKARI":
                yon="SOL"
                x-=hiz/100
                arabaResim = pygame.transform.rotate(arabaResim, +90)
            elif yon=="SOL":
                x-=hiz/100
            elif yon=="ASAGI":
                yon="SOL"
                x-=hiz/100
                arabaResim = pygame.transform.rotate(arabaResim, -90)
            elif yon=="SAG":
                x-=hiz/100
        if pygame.key.get_pressed()[sagtus]:
            if yon=="YUKARI":
                yon="SAG"
                x+=hiz/100
                arabaResim = pygame.transform.rotate(arabaResim, -90)
            elif yon=="SOL":
                x+=hiz/100
            elif yon=="ASAGI":
                yon="SAG"
                x+=hiz/100
                arabaResim = pygame.transform.rotate(arabaResim, +90)
            elif yon=="SAG":
                x+=hiz/100
        if pygame.key.get_pressed()[yukaritus]:
            if yon=="YUKARI":
                y-=hiz/100
            elif yon=="SOL":
                yon="YUKARI"
                y-=hiz/100
                arabaResim = pygame.transform.rotate(arabaResim, -90)
            elif yon=="ASAGI":
                y-=hiz/100
            elif yon=="SAG":
                yon="YUKARI"
                y-=hiz/100
                arabaResim = pygame.transform.rotate(arabaResim, +90)
        if pygame.key.get_pressed()[asagitus]:
            if yon=="YUKARI":
                y+=hiz/100
            elif yon=="SOL":
                yon="ASAGI"
                y+=hiz/100
                arabaResim = pygame.transform.rotate(arabaResim, +90)
            elif yon=="ASAGI":
                y+=hiz/100
            elif yon=="SAG":
                yon="ASAGI"
                y+=hiz/100
                arabaResim = pygame.transform.rotate(arabaResim, -90)
     
        Screen.blit(surface,(0,0))
        arabakonum=pygame.Rect(x,y,arabawidth,arabaheight)
        Screen.blit(arabaResim, arabakonum)          # arabayı oyuna yükleme
        pygame.display.update()
main()
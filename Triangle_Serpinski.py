import math,sys,pygame,random
pygame.init()

screen=pygame.display.set_mode((1000,600))
screen.fill((0,0,0))

polygon=[(500,50),(250,550),(750,550)]

pointX=random.randint(250,750)
pointY=random.randint(50,550)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    for i in range(500):
        pygame.draw.circle(screen,(250,250,250),(pointX,pointY),1)
        nrdm=random.randint(0,2)
        pointX=(pointX+polygon[nrdm][0])/2
        pointY=(pointY+polygon[nrdm][1])/2
    pygame.display.flip()

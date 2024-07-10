import pygame,sys,math,random
pygame.init()

screen=pygame.display.set_mode((1000,600))
screen.fill((0,0,0))
nbside=5
diviseur=2.4
pointX=500
pointY=300

polygon=[[0 for _ in range(2)] for _ in range(nbside)]
nbrdm2=0
def coord_polygon(nbside):
    for i in range(nbside):
        for j in range(2):
            if j==0:
                polygon[i][j]=500+280*math.cos(math.pi/2+i*((2*math.pi)/nbside))
            if j==1:
                polygon[i][j]=300-280*math.sin(math.pi/2+i*((2*math.pi)/nbside))

coord_polygon(nbside)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    for i in range(5000):
        pygame.draw.circle(screen,(250,250,250),((diviseur-1)*pointX,(diviseur-1)*pointY),1)
        nbrdm=random.randint(0,len(polygon)-1)
        if(nbrdm2!=nbrdm):
            nbrdm2=nbrdm
            pointX=(pointX+polygon[nbrdm][0])/diviseur
            pointY=(pointY+polygon[nbrdm][1])/diviseur
    pygame.display.flip()

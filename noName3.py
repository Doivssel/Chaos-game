import pygame,sys,math,random
pygame.init()

screen=pygame.display.set_mode((1000,600))
screen.fill((0,0,0))
nbside=7
diviseur=2.5
pointX=500
pointY=300

polygon=[[0 for _ in range(2)] for _ in range(nbside)]


def coord_polygon(nbside):
    for i in range(nbside):
        for j in range(2):
            if j==0:
                polygon[i][j]=500+280*math.cos(math.pi/2+i*((2*math.pi)/nbside))
            if j==1:
                polygon[i][j]=300-280*math.sin(math.pi/2+i*((2*math.pi)/nbside))

coord_polygon(nbside)

nbrdm2=-1

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    for i in range(25):
        pygame.draw.circle(screen,(250,250,250),((diviseur-1)*pointX,(diviseur-1)*pointY),1)
        nbrdm=random.randint(0,len(polygon)-1)
        if(nbrdm==nbrdm2):
            pointX=(pointX+polygon[nbrdm][0])/diviseur
            pointY=(pointY+polygon[nbrdm][1])/diviseur  
            pygame.draw.circle(screen,(250,250,250),((diviseur-1)*pointX,(diviseur-1)*pointY),1)     
            if(nbrdm==0):
                while(nbrdm==0 or nbrdm==4 or nbrdm==1):
                    nbrdm=random.randint(0,len(polygon)-1) 
            elif(nbrdm==4):
                while(nbrdm==0 or nbrdm==4 or nbrdm==3):
                    nbrdm=random.randint(0,len(polygon)-1) 
            else:
                while(nbrdm==nbrdm2 or nbrdm==nbrdm2-1 or nbrdm==nbrdm2+1):
                    nbrdm=random.randint(0,len(polygon)-1)
            pointX=(pointX+polygon[nbrdm][0])/diviseur
            pointY=(pointY+polygon[nbrdm][1])/diviseur
            nbrdm2=-1
        else:
            nbrdm2=nbrdm
            pointX=(pointX+polygon[nbrdm][0])/diviseur
            pointY=(pointY+polygon[nbrdm][1])/diviseur
    pygame.display.flip()
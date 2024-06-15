import pygame,sys,math,random
pygame.init()

screen=pygame.display.set_mode((1000,600))
screen.fill((0,0,0))
nbside=4
diviseur=3
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

#c'est sympa mettre 3 en diviseur et 4 en nbside
#polygon.append([(polygon[3][0]+polygon[1][0])/2,(polygon[0][1]+polygon[2][1])/2])

polygon.append([(polygon[0][0]+polygon[1][0])/2,(polygon[0][1]+polygon[1][1])/2])
polygon.append([(polygon[1][0]+polygon[2][0])/2,(polygon[1][1]+polygon[2][1])/2])
polygon.append([(polygon[2][0]+polygon[3][0])/2,(polygon[2][1]+polygon[3][1])/2])
polygon.append([(polygon[3][0]+polygon[0][0])/2,(polygon[3][1]+polygon[0][1])/2])

print(polygon)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    for i in range(25):
        pygame.draw.circle(screen,(250,250,250),((diviseur-1)*pointX,(diviseur-1)*pointY),1)
        nbrdm=random.randint(0,len(polygon)-1)
        pointX=(pointX+polygon[nbrdm][0])/diviseur
        pointY=(pointY+polygon[nbrdm][1])/diviseur
    pygame.display.flip()
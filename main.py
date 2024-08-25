import pygame
import random
import numpy as np
import math
pygame.init

ballcount = 0
hitcount = 0
screenWidth = 1200
screenHeight = 700
color = [(255,0,0),(0,0,255),(0,255,0)]
team=[]
x=[]
y=[]
object=[]
speed_range=(2,7)
direction = [1,-1]
radius = 15
num_of_A = 50

def distance(x1, y1, x2, y2):
    dsq = (x1 - x2) ** 2 + (y1 - y2) ** 2
    d = np.sqrt(dsq)
    return d

def separate_balls(ballX, ballY, otherX, otherY):

    angle = - math.atan2(ballY - otherY, ballX - otherX)

    diffR = radius + radius - distance(ballX, ballY, otherX, otherY)
    diffR *= 0.5

    ballX -= math.cos(angle) * diffR
    ballY -= math.sin(angle) * diffR

    otherX -= math.cos(angle) * diffR
    otherY -= math.sin(angle) * diffR

window = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Power Group")

run=True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((0,0,0))

    while ballcount<num_of_A:
        newX = random.randint(2*radius,990)
        newY = random.randint(2*radius,490)
        newSpeedX = random.randint(*speed_range) * random.choice(direction)
        newSpeedY = random.randint(*speed_range) * random.choice(direction)
        overlapped = False
            
        if ballcount>0:
            for j in range(0,ballcount):
                d = distance(newX, newY, object[j]['x'],object[j]['y'])
                if d < 2*radius:
                    overlapped = True
                    break

        if overlapped == False:
            x.append(newX)
            y.append(newY)
            object.append({'x': x[ballcount], 'y': y[ballcount], 'speedX': newSpeedX, 'speedY': newSpeedY, 'team': random.randint(0,2)})
            ballcount+=1
        else:
            continue

    for i in range(len(object)):
        object[i]['x'] += object[i]['speedX']
        object[i]['y'] += object[i]['speedY']

        if object[i]['x'] >= screenWidth:
            object[i]['x'] = screenWidth
            object[i]['speedX'] *= -1
        if object[i]['x']  <= 0:
            object[i]['x']  = 0
            object[i]['speedX'] *= -1
        if object[i]['y'] >= screenHeight:
            object[i]['y'] = screenHeight
            object[i]['speedY'] *= -1
        if object[i]['y']  <= 0:
            object[i]['y']  = 0
            object[i]['speedY'] *= -1

    for i in range(len(object)):
        hitcount = 0
        while hitcount < num_of_A:
            if hitcount == i:
                hitcount += 1
                continue

            d2 = distance(object[hitcount]['x'], object[hitcount]['y'], object[i]['x'],object[i]['y'])

            if d2 <= 2*radius:

                separate_balls(object[hitcount]['x'], object[hitcount]['y'], object[i]['x'],object[i]['y'])

                if object[hitcount]['team'] != object[i]['team']:
                    if object[hitcount]['team']==0 and object[i]['team']==1:
                        object[hitcount]['team']=1
                    elif object[hitcount]['team']==0 and object[i]['team']==2:
                        object[i]['team']=0
                    elif object[hitcount]['team']==1 and object[i]['team']==2:
                        object[hitcount]['team']=2
                    elif object[hitcount]['team']==1 and object[i]['team']==0:
                        object[i]['team']=1
                    elif object[hitcount]['team']==2 and object[i]['team']==0:
                        object[hitcount]['team']=0
                    elif object[hitcount]['team']==2 and object[i]['team']==1:
                        object[i]['team']=2

                if object[i]['speedX'] >0:
                    object[i]['speedX'] = random.randint(*speed_range) * -1
                else:
                    object[i]['speedX'] = random.randint(*speed_range)

                if object[i]['speedY'] >0:
                    object[i]['speedY'] = random.randint(*speed_range) * -1
                else:
                    object[i]['speedY'] = random.randint(*speed_range)

                if object[hitcount]['speedX'] >0:
                    object[hitcount]['speedX'] = random.randint(*speed_range) * -1
                else:
                    object[hitcount]['speedX'] = random.randint(*speed_range)

                if object[hitcount]['speedY'] >0:
                    object[hitcount]['speedY'] = random.randint(*speed_range) * -1
                else:
                    object[hitcount]['speedY'] = random.randint(*speed_range)

            hitcount += 1
        
    for i in range(len(object)):
        pygame.draw.circle(window, color[object[i]['team']], (object[i]['x'], object[i]['y']), radius)
        
    pygame.display.update()

pygame.quit()
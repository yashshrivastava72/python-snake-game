import pygame
import time
import random
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
yellow=(255,201,14)
green=(0,255,0)
brown=(190,94,5)
orange=(249,123,11)
purple=(136,99,245)
gray=(141,112,141)
lgray=(178,178,178)
display_width=800
display_height=600
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('snake') 
block_size=20
fps=30
clock=pygame.time.Clock()
font=pygame.font.SysFont("comicsansms",40)
def pres():
    pres=True
    while pres:
        gameDisplay.fill(lgray)
        message("BY YASH SHRIVASTAVA",brown,-200)
        message("ENROLLMENT NUMBER-151450",orange,-100)
        message("BATCH=B7",yellow,-50)
        message("Press c to continue",black,0)
        pygame.display.update()
        clock.tick(5)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    pres=False
                    gameintro()
        
def pause():
    paused=True
    while paused: 
        message("PAUSED",black,-100)
        message("press c to continue or q to quit",white)
        pygame.display.update()
        clock.tick(5)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    paused=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
            
            
            
                    
def score(score):
    text=font.render("SCORE :"+str(score),True,black)
    gameDisplay.blit(text,[0,0])
def gameintro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    intro=False
                    gameloop()
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        
        gameDisplay.fill(white)
        message("welcome to snake",green,-200)
        message("the objective of the game is to eat apples",black,-30)
        message("the more apples you eat the longer u get",black,10)
        message("if you run into yourself or edges,then die",black,50)
        message("press c to play or q to quit p to pause",black,180)
        pygame.display.update()
        clock.tick(5)
        
def snake(block_size,snakelist):
    for xny in snakelist:
        pygame.draw.rect(gameDisplay,yellow,[xny[0],xny[1],block_size,block_size])
def text_objects(text,color):
    
    textSurface=font.render(text,True,color)
    return textSurface,textSurface.get_rect()


def message(msg,color,y_displace=0):
    textSurf,textRect=text_objects(msg,color)
    textRect.center=(display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)
def gameloop():
    gameExit=False
    gameOver=False
    lead_x=display_width/2
    lead_y=display_height/2
    lead_x_change=0
    lead_y_change=0
    snakelist=[]
    snakelength=1
    randApplex=round(random.randrange(0,display_width-block_size)/20)*20    
    randAppley=round(random.randrange(0,display_height-block_size)/20)*20   
    while not gameExit:
        if gameOver==True:
            message("game over",red,-70)
            message("press c to play again or q to quit",green,50)
            pygame.display.update()
        while gameOver==True:
           
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameOver=False
                    gameExit=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_c:
                        gameloop()
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False
                    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    lead_x_change=-block_size
                    lead_y_change=0
                if event.key==pygame.K_RIGHT:
                    lead_x_change=block_size
                    lead_y_change=0
                if event.key==pygame.K_UP:
                    lead_y_change=-block_size
                    lead_x_change=0
                if event.key==pygame.K_DOWN:
                    lead_y_change=block_size
                    lead_x_change=0
                if event.key==pygame.K_p:
                    pause()
        if lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<0:
            gameOver=True
            
            
        lead_x+=lead_x_change
        lead_y+=lead_y_change
        gameDisplay.fill(gray)
        pygame.draw.rect(gameDisplay,red,[randApplex,randAppley,block_size,block_size])                                
        
        
        snakehead=[]
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        snake(block_size,snakelist)
        score(snakelength-1) 
        if len(snakelist)>snakelength:
            del snakelist[0]
        for eachSegement in snakelist[:-1]:
            if eachSegement==snakehead:
                gameOver=True
        pygame.display.update()
        clock.tick(fps)
        if lead_x==randApplex and lead_y==randAppley:
            randApplex=round(random.randrange(0,display_width-block_size)/20)*20
            randAppley=round(random.randrange(0,display_height-block_size)/20)*20
            snakelength+=1
        
               
        clock.tick(fps)
    pygame.display.quit()
    quit()
pres()
gameintro()    
gameloop()        


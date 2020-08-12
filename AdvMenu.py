#imports Modules
import pygame, sys, os

#setup window
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Adventure Game")
screen = pygame.display.set_mode((500,500),0,False)
rootDirectory = os.path.dirname(__file__)
imageDirectory = rootDirectory +'\\img'
textDirectory = rootDirectory +'\\text'



TitleFont = pygame.font.SysFont(None,50)
NormalFont = pygame.font.SysFont(None,30)

#Title
Title = TitleFont.render("Adventure Game",1,(255,255,255))
Titlerect = Title.get_rect()
Titlerect.topleft = (20,20)

#Clicks
click = False
rightClick = False

#Button
btnStart = pygame.draw.rect(screen,(100,250,50),(30,175,150,40))
txtStart = NormalFont.render("Start",1,(0,0,0))
txtStartrect = txtStart.get_rect()
txtStartrect.center = (80,200)
#Buttons for Answers
btnAnswer1 = None
btnAnswer2 = None
btnAnswer3 = None
btnAnswer4 = None 
#Other Field Variables
mouseX, mouseY = pygame.mouse.get_pos()
questionCount = 0
currentQuestions = []

pygame.display.update()


def grabFile(fileName):

    #[Type of Sentence (Sentence/Question)][The actual words said]
    dialogue = open(textDirectory +'\\' + fileName + '.txt')
    #local variables that can be used in either if statement
    myCount = 0
    tempArray1 = []
    
    if fileName == "text":
        #local variables that can only be used in this if statement
        tempArray2 = []
        
        for line in dialogue:
            tempArray1.insert(myCount,line)
            tempArray2.insert(myCount,dialogue.readline())
            myCount = myCount + 1

        
        textArray = [tempArray1,tempArray2]
    elif fileName == "questions":
        #local variable
        #TODO: changeing Delimiters to a comma
        tempString = ""
        for line in dialogue:
            if questionCount == myCount:
                tempString = dialogue.readline()
            else:
                myCount = myCount + 1
        #print(tempString)
        #We need to turn the string into a delimited array
        textArray = tempString.split(",")


    dialogue.close()
    return textArray

def fpsAndMouse():
    #FPS
    myFPS = NormalFont.render(str(round(mainClock.get_fps(),2)),1,(255,10,10))             
                
    myFPSrect = myFPS.get_rect()
    myFPSrect.topleft = (400,30)
    screen.blit(myFPS,myFPSrect)
        
    mouseX, mouseY = pygame.mouse.get_pos()
    #shows the x and y of the mouse real time
    xAndy = NormalFont.render("(" + str(mouseX) + ", " + str(mouseY) + ")",1,(255,255,255))                      
    xAndyrect = xAndy.get_rect()
    xAndyrect.topleft = (mouseX+15,mouseY-15)
    screen.blit(xAndy,xAndyrect)
    return mouseX,mouseY

#sends in dialouge and puts it on screen
def createText(text):
    txtBox = NormalFont.render(text,1,(0,0,0))
    txtBoxrect = txtBox.get_rect()
    txtBoxrect.topleft = (20,390)
    screen.blit(txtBox,txtBoxrect)

#create buttons to click for answering questions
def createAnswers(text):
    #parameter: Array that has the answers in them
    #TODO: Create as many buttons as needed
    #Create text on top of the buttons
    #Be able to click the buttons



def gameScreen():
    secondWhile = True
    clickCount = 0
    click = False
    questionCount = 0
    clickcounter = True
    while secondWhile == True:
        
        #makes the background black
        screen.fill((0,0,0))
        
        myImage = pygame.transform.smoothscale(
            pygame.image.load(imageDirectory + "\\fluffy-clouds.jpg")
            ,(500,376)
        )
        screen.blit(myImage,(0,0))         #   x y    width height
        pygame.draw.rect(screen,(255,255,255),(0,375,500,125),0)
        pygame.draw.rect(screen,(135,179,120),(20,390,460,95),0)
        

        mouseX, mouseY = fpsAndMouse()

        #Where to do run game
        
        #Displays text until at the end of the array
        #if clickCount < len(myText[1]):
        #    createText(myText[1][clickCount])

        #If the category is question
        if myText[0][clickCount]=="Question\n":

                createText(myText[1][clickCount])
                #create a text box below the normal text
                #just for the questions

                questionCount = questionCount + 1
                clickcounter = False
        #if the category is sentence
        elif myText[0][clickCount]=="Sentence\n":
                createText(myText[1][clickCount])
        
        if clickcounter == True:
            
        #goes to the next index when you click
            if click == True :
                clickCount = clickCount + 1


        #Where to stop code for gameplay
        click = False


        rightClick = False     

        
        


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                else:
                    rightClick = True

        pygame.display.update()
        mainClock.tick(60)




        
   
    
def titleScreen():
    firstWhile = True
    while firstWhile == True:

        #TODO: make some epic backgrounds
        titleImage = pygame.image.load(imageDirectory + "\\titleScreenBackground.jpg")
        screen.blit(titleImage,(0,0))
        

        #draws the button
        btnStart = pygame.draw.rect(screen,(100,250,50),(30,175,150,40))
        #moved blits to the while true
        screen.blit(txtStart,txtStartrect)
        screen.blit(Title,Titlerect)

        mouseX, mouseY = fpsAndMouse()

        #Our first Button click event
        if btnStart.collidepoint((mouseX,mouseY)):
            if click == True:
                #do someting
                firstWhile = False
                gameScreen()
                

        
        
       
        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
        #updates the display
        pygame.display.flip()
        mainClock.tick(60)


myText = grabFile("text")
titleScreen() 








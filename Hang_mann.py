import pygame
import math

pygame.init()

window=pygame.display.set_mode((1000,700))
pygame.display.set_caption("Hangman Game Man")

Start=pygame.image.load("./image/dev.jpg")
Start=pygame.transform.scale(Start,(1000,700)).convert_alpha()

Enter=pygame.image.load("./image/Enter.png")
Enter=pygame.transform.scale(Enter,(400,220)).convert_alpha()

Hell=pygame.image.load("./image/Hell.png")
Hell=pygame.transform.scale(Hell,(400,220)).convert_alpha()

game_over=pygame.image.load("./image/game_over.jpg")
game_over=pygame.transform.scale(game_over,(1000,700)).convert_alpha()

Main=pygame.image.load("./image/main.jpg")
Main=pygame.transform.scale(Main,(1000,700)).convert_alpha()

clock=pygame.time.Clock()

font=pygame.font.SysFont('comicsans',40)

star_x=150
star_y=550
radius=20
gap=15
latters=[]
A=65  

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)   
    window.blit(screen_text,[x,y])


for i in range(26):
    x=star_x+gap*2+((radius*2+gap)*(i%13))
    y=star_y+((i//13))*((gap+radius*2))
    latters.append((x,y,chr(A+i)))



images=[]
for i in range(6):
    image=pygame.image.load("./image/hangman"+str(i)+".png")
    image=pygame.transform.scale(image,(209,216))

    images.append(image)






hangman_status=0
words="DEVELOPER"
guessed=[]
    



def welcome():
    fun=True
    while fun:
        clock.tick(60)
        window.fill((255,255,255))
        window.blit(Start,(0,0))
        window.blit(Enter,(300,400))
        window.blit(Hell,(300,10))
        
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fun=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    
                    loop() 
            pygame.display.update()
        
        

    
            

                          
def draw():

    window.fill((255,255,255))
    window.blit(Main,(0,0))

    display_word=" "
    for latter in words:
    
        
        if latter in guessed:
            display_word+=latter+" "
        else:
            display_word+="_"+" "
    text_screen(display_word,(0,0,0),400,400)

    for le in latters:
        x,y, lt =le
        pygame.draw.circle(window,(0,0,0),(x,y),radius,3)
        text=font.render(lt,1,(0,0,0))
        window.blit(text,(x-10,y-10))


    window.blit(images[hangman_status],(460,170))  
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    window.fill((255,255,255))
    window.blit(game_over,(0,0))
    text =font .render(message, 1, (255,255,255))
    window.blit(text, (500,500))
    pygame.display.update()
    pygame.time.delay(3000)

def loop():
    run =True
    global hangman_status
    clock=pygame.time.Clock()
    # veriable



    while run:
        clock.tick(60)
        

       
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                

            if event.type==pygame.MOUSEBUTTONDOWN:
                m_x,m_y=pygame.mouse.get_pos()
                for lerrer in latters:
                    x,y,lt=lerrer
                    dic=math.sqrt((x-m_x)**2+(y-m_y)**2)
                    if dic<radius:
                        guessed.append(lt)
                        if lt not in words:
                            hangman_status+=1

        
        
        draw()
        won = True
        for letter in words:
            if letter not in guessed:
                won = False
                
        
        if won:
            display_message("You Won!")
            break

        if hangman_status ==6:
            display_message("You LOST!")
            break    


welcome()
loop()
pygame.quit()








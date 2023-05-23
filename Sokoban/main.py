import pygame
from counst import *
Map = []
Start = []
man_pos = []
chest_final = []
chest_pos = []
x_0 = 0
y_0 = 0


move_com = {"a":(0,-1),"d":(0,1),"s":(1,0),"w":(-1,0)}


# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sokuban")
clock = pygame.time.Clock()
running = True
def print_map():
# Start[] : first is people postion, then is chest pos and chest final pos
    for i in Map:
        print(i)
    print()
    #print(Start)
    #print(man_pos)
    #print(chest_pos)

def load_map(level):
    global Map,Start,man_pos,chest_final,chest_pos,x_0,y_0
    Map = []
    Start =[]
    filename = f"map{level}.txt"
    with open(filename,"r") as file:
        for line in file:
            L = [eval(i) for i in line.split()]
            Map.append(L)
    Start = Map.pop()
    #update pos
    man_pos = []
    chest_pos = []
    chest_final = []
    #man pos
    man_pos= [(Start[0],Start[1])]
    x_0 = Start[0]
    y_0 = Start[1]

    n = len(Start)
    #chest post
    for i in range(2,n,4):        
        chest_pos.append((Start[i],Start[i+1]))
        chest_final.append((Start[i+2],Start[i+3]))

def New_game():
    load_map(level)
    
def update_people(x,y):
    m = len(Map)
    n = len(Map[0])
    global x_0,y_0
    if (Map[x + x_0][y + y_0] !=1): #check in the map
        
        if m> x + x_0 >=0 and n> y + y_0 >=0:
            if (x_0,y_0) in chest_final:
                if(x+x_0,y+y_0) in chest_pos and (2*x+x_0,2*y+y_0)not in chest_pos and  Map[2*x+x_0][2*y+y_0] != 1:
                    Map[x_0][y_0] = 4
                    His_man = (x_0,y_0)
                    x_0 = x + x_0
                    y_0 = y + y_0
                    man_pos.append((x_0,y_0))
                    Map[x_0][y_0] = 2
                    update_chest(x,y)

                elif((x+x_0,y+y_0) not in chest_pos):
                    Map[x_0][y_0] = 4
                    His_man = (x_0,y_0)
                    x_0 = x + x_0
                    y_0 = y + y_0
                    Map[x_0][y_0] = 2
                    man_pos.append((x_0,y_0))

            
            else:
                #neu khong co chest
                if ((x+x_0,y+y_0) not in chest_pos):
                    Map[x_0][y_0] = 0
                    His_man = (x_0,y_0)
                    x_0 = x + x_0
                    y_0 = y + y_0
                    Map[x_0][y_0] = 2
                    man_pos.append((x_0,y_0))
                if ((x+x_0,y+y_0) in chest_pos and (2*x+x_0,2*y+y_0)not in chest_pos and Map[2*x+x_0][2*y+y_0] != 1):
                    Map[x_0][y_0] = 0
                    x_0 = x + x_0
                    y_0 = y + y_0
                    Map[x_0][y_0] = 2
                    update_chest(x,y)
                    man_pos.append((x_0,y_0))

                

def update_chest(x,y): 
    x_1 = x_0+x
    y_1 = y_0 +y
    if (x_1,y_1) not in chest_pos:
        chest_pos.remove((x_0,y_0))
        chest_pos.append((x_1,y_1))
        Map[x_1][y_1] = 3
        if (x_1,y_1) in chest_final:
            hightline()
    
def hightline():
    print("good")

def win_game():
    if set(chest_pos) == set(chest_final):
        return True

def Reset():
    New_game()
def Back():
    pass
def update_map():
    m = len (Map)
    n = len(Map[0])
    for i in range(m):
        for j in range(n):
            if Map[i][j] == 1: #WALL
                pygame.draw.rect(screen,BLACK,((j)*40,(i) * 40,40,40))
            if Map[i][j] == 2: 
                pygame.draw.rect(screen,YELLOW,((j)*40,(i) * 40,40,40))
            if Map[i][j] == 3 :
                pygame.draw.rect(screen,GREEN,((j)*40,(i) * 40,40,40))
            if Map[i][j] == 4 :
                pygame.draw.circle(screen,RED,((j)*40+20,(i) *40+ 20),10)

screen = pygame.display.set_mode((800, 600))
level = int(input("Load level\n"))

New_game()
print_map()
while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    pygame.draw.rect(screen,WHITE ,(600,0,200,600))
    clock.tick(60)  # limits FPS to 60

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    #Create Map
    
    update_map()
                
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                # print("A")
                XY = move_com["a"]
                update_people(XY[0],XY[1])
                update_map()
                print_map()
            if event.key == pygame.K_s:
                # print("S")
                XY = move_com["s"]
                update_people(XY[0],XY[1])
                update_map()
                print_map()
            if event.key == pygame.K_d:
                # print("D")        
                XY = move_com["d"]
                update_people(XY[0],XY[1])
                update_map()
                print_map()
            if event.key == pygame.K_w:
                # print("W")
                XY = move_com["w"]
                update_people(XY[0],XY[1])
                update_map()
                print_map()
            if event.key == pygame.K_SPACE:
                Reset()
            if event.key == pygame.K_BACKSPACE:
                Back()
    if win_game() == True:
        if level + 1 <=3:
            level +=1
            New_game()
        else : 
            pass

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()


pygame.quit()
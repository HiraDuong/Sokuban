#0 is space , 1 is wall, 2 is start postion(people), 3 is chest , 4 is chest final pos
# start : first is people postion, after is chest
Map = []
Start = []
man_pos = []
chest_final = []
chest_pos = []
x_0 = 0
y_0 = 0
def print_map():
# Start[] : first is people postion, then is chest pos and chest final pos
    for i in Map:
        print(i)
    print()
    #print(Start)

def load_map(level):
    global Map,Start,man_pos,chest_final,chest_pos,x_0,y_0
    Map = []
    Start =[]
    filename = f"Sokoban/map{level}.txt"
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

def update_people(x,y):
    m = len(Map)
    n = len(Map[0])
    global x_0,y_0
    if (Map[x + x_0][y + y_0] !=1): #check in the map
        if m> x + x_0 >=0 and n> y + y_0 >=0:
            if (x_0,y_0) in chest_final:
                Map[x_0][y_0] = 4
            
            else:
                if ((x+x_0,y_0+y) not in chest_pos or (x_0+2*x,y_0+2*y) not in chest_pos):
                    Map[x_0][y_0] = 0
                    x_0 = x + x_0
                    y_0 = y + y_0
                    if (x_0,y_0) in chest_pos:
                            update_chest(x,y)
                    Map[x_0][y_0] = 2
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

#####################################################################

#START GAME   
level = int(input("Nhập level: "))
load_map(level)#  
print_map()

while(1):
    command = input()
    move_com = {"a":(0,-1),"d":(0,1),"s":(1,0),"w":(-1,0)}
    XY = move_com[command]
    update_people(XY[0],XY[1])
    print_map()
    #print(chest_pos)
    #print(chest_final)
    if win_game() == True:
        print("You won the game")
        level += 1
        load_map(level)
        print_map()
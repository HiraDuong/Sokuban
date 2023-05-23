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
def build_house(my_dream,color):
    house = False
    roof_color = color[0]
    house_color = color[1]
    door_color = color[2]
    roof = my_dream[0]
    walls = my_dream[1]
    
    while not house:
        roof_stat = build_walls(walls, roof_color)
        walls_stat = build_walls(walls, house_color)
        door_stat = build_door(door_color, door_color)
        if roof_stat == True and walls_stat == True and door_stat == True:
            house = True
            print('Вы завершили свой дом мечты!')

    return house

        

def build_roof(r,rs):
    return True

    

def build_walls(r,ws):
    return True
    

def build_door(r,dc):
    return True
    

    
idea = ('roof','walls')
color = ('red','white','blue')
build_house(idea,color)



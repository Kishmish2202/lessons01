ban_world = ['hello','world','tartar']

def ban_worlds(x):
    for i in x[:]:
        for u in ban_world:
            if i == u:
                x.remove(i)
                
    return x
           
            
        




print(ban_worlds(['tartar','Чайлд','hello']))
print(ban_worlds(['hello', 'my','world']))
print(ban_worlds(['тортик','очень','вкусный']))
print(ban_worlds(['hello','world','hello']))

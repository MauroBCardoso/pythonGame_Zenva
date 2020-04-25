#Python language (Functions)


x_pos = 0
e_x_pos = 4
print(x_pos)

def move():
    global x_pos
    x_pos += 1


move()



def move_by(amount):
    global x_pos
    x_pos += amount


def check_for_collision():
    global x_pos
    global e_x_pos
    if x_pos == e_x_pos:
        return True
    else:
        return False

move_by(5)

did_collide = check_for_collision()

    
print(x_pos)
print(did_collide)


#Python (classes and objects)

class GameCharacter:

    speed = 5 # the moment it is created it has the value
    
    def __init__(self, name, width, height, x_pos, y_pos):     #self is GameCharacter
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount


character_0 = GameCharacter('char', 50, 100, 100, 100)

print(character_0.name)

character_0.name = 'changed'

print(character_0.name)

character_0.move(50, 100)

print(character_0.x_pos)
print(character_0.y_pos)

#Python subclasses, superclasses, and inheritance


class PlayerCharacter(GameCharacter):

    speed = 10
    
    def __init__(self, name, width, height, x_pos, y_pos):
        super().__init__(name, width, height, x_pos, y_pos)
        
    def move(self, by_y_amount):
        super().move(0, by_y_amount)
player = PlayerCharacter('player', 100, 100, 500, 500)
print(player.name)
player.move(100)
print(player.x_pos)
print(player.y_pos)

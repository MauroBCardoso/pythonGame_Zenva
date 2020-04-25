#Python basics (collections)

#Tuples
size = (100,200)

print(size)

width = size[0]
height = size[1]

new_size = size + (300, )
print(new_size)

del new_size #no longer exists

len (size) #2
max (size) #200
min (size) #100

does_contain = 100 in size #does_contain = True

print(does_contain)

#Array/list
movement = [5,-2, -3, 4, -1]
first_movement = movement[0] #first_movement = 5
movement [0] = 7 #movement = [7,-2, -3, 4, -1]
movement.append(-5) #movement = [7,-2, -3, 4, -1,-5]
movement.remove(-3) #movement = [7,-2, 4, -1,-5]


#Dictionaries

starting_position = {'p_0': 50, 'p_1': 100, 'p_2': 150}
starting_position['p_0'] #50
starting_position.keys() #['p_0', 'p_1' , 'p_2']

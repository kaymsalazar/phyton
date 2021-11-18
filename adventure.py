import random
#Kaylean Ramirez Salazar
#Luz Reyes
#Chelsea Rubio
room_list = []
room = []
room = ["You are in a stinky room, you see another room to the north, and a hallway to the east. ",3,1,None,None]
room_list.append(room)
room = ["You are in a Hallway; you go to the north and see a portal",4,2,None,0]
room_list.append(room)
room = ["You are currently walking into the dining room",5,None,None,1]
room_list.append(room)
room = ["Yur moms room",None,4,0,None,""]
room_list.append(room)
room = ["You are in a portal", 6,5,1,3]
room_list.append(room)
room = ["Your in Jessica's room ",None,None,2,4]
room_list.append(room)
room = ["You are in a room that is surprisingly clean", None,None,4,1]
room_list.append(room)
current_room = 0
done = False
next_room = ""
while not done:
chance = random.randrange(1,3)
if current_room == 3:
if chance == 2:
print("You jumped out a window and died,resurected and went into a random room")
print(room_list[current_room]
[0]
)
direction = input("What do you want to do? ")
if direction == "n":
next_room = room_list[current_room]
[1]
elif direction == "e":
next_room = room_list[current_room]
[2]
elif direction == "s":
next_room - room_list[current_room]
[3]
elif direction == "w":
next_room = room_list[current_room]
[4]
else:
print()
print("I don't understand.")
if next_room == "None":
print("You can't go that way!")
else:
current_room = next_room

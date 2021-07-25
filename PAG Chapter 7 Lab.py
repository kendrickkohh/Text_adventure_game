room_list = []

room = ["You are in the Master Bedroom. It is cosy here.\nThere are doors to the North and East", 3, 1, None, None] #Room 0
room_list.append(room) 

room = ["You are in the South Hall.\nThere is a passage to the North, East and West.", 4, 2, None, 0] #Room 1
room_list.append(room)

room = ["You are in the Dining Room. It looks like a roast is being made for supper.\nA hallway is to the North and West", 5, None, None, 1] #Room 2
room_list.append(room)

room = ["You are in the spare bedroom. It looks like the sheets have yet to be changed.\nThere are doors to the East and South.", None, 4, 0, None] #Room 3
room_list.append(room)

room = ["You are in the North Hall.\nThere are hallways leading in all directions", 6, 5, 1, 3] #Room 4
room_list.append(room)

room = ["You are in the Kitchen. There is a smell of delicious pie in the air.\nThere are doors to the South and West.", None, None, 2, 4] #Room 5
room_list.append(room)

room = ["You are in the Balcony. Take a breath of fresh air.\nThere is one door to your South", None, None, 4, None] #Room 6
room_list.append(room)

current_room = 0

done = False

while not done:
    print()
    print(room_list[current_room][0])
    x = input("What direction will you proceed? ")
    x = x.lower()

    if x == "north" or x == "n":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room

    elif x == "east" or x == "e":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You cant go that way")
        else:
            current_room = next_room

    elif x == "south" or x == "s":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You cant go that way")
        else:
            current_room = next_room

    elif x == "west" or x == "w":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You cant go that way")
        else:
            current_room = next_room

    elif x == "quit" or x == "q":
        quit()

    else:
        print("Please type in a direction(East/E).")

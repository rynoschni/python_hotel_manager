hotel = {
  1: {
    101: ['George Jefferson', 'Wheezy Jefferson'],
  },
  2: {
    237: ['Jack Torrance', 'Wendy Torrance'],
  },
  3: {
    333: ['Neo', 'Trinity', 'Morpheus']
  }
}

def start_check_in_or_out():
    checkinout = None
    while checkinout == None:
        checkinout = input("Are you checking in, or out?").lower()
        if checkinout == 'in' or checkinout == 'out':
            return checkinout
        else:
            print('I\'m sorry, I only understand "in" or "out". Please reply with "in" or "out."')
            checkinout = None

def get_room_and_floor():
    floor = int(input('Which floor would you prefer?'))
    room = int(input('Which room would you prefer?'))
    return floor, room

def is_room_empty(floor, room):
    if floor in hotel.keys():
        if room in hotel[floor].keys() and len(hotel[floor][room]) > 0:
            return False
        else:
            return True
    else:
        return True
    return False

def do_checkin(location):
    occupant = input('What is your name?')
    if location[0] in hotel.keys():
        hotel[location[0]][location[1]] = occupant
    else:
        hotel[location[0]] = {}
        hotel[location[0]][location[1]] = occupant
    return True

def do_checkout(location):
    del hotel[location[0]][location[1]]
    return True

run = True

while run == True:
    status = start_check_in_or_out()
    if status == 'in':
        checked_in = False
        while checked_in == False:
            location = get_room_and_floor()
            room_empty = is_room_empty(location[0], location[1])
            if room_empty == True:
                checked_in = do_checkin(location)
            else:
                print("That room is occupied, please choose another room.")
                checked_in = False

    elif status == 'out':
        checked_out = False
        while checked_out == False:
            location = get_room_and_floor()
            room_empty = is_room_empty(location[0], location[1])
            if room_empty == True:
                print("There isn't anyone in that room.")
                checked_out = False
            else:
                checked_out = do_checkout(location)
    print(hotel)
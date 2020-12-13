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
    # Default value is None
    checkinout = None
    # This loop will keep going until the user replies with "in" or "out."
    # This removes one of our potential issues.
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

# Let's verify the room's status.
def is_room_empty(floor, room):
    # Let's check the rooms
    print(hotel.keys())
    # Is this floor in the hotel?
    if floor in hotel.keys():
        #If so, is the room on this floor?
        if room in hotel[floor].keys() and len(hotel[floor][room]) > 0:
            # We have a room, is it full?
            return False
        else:
            return True
    else:
        # Floor doesn't exist, ergo the room is empty
        return True
    # Default value, assumes room exists and is occupied
    return False

def do_checkin(location):
    occupant = input('What is your name?')
    if location[0] in hotel.keys():
        hotel[location[0]][location[1]] = occupant
    else:
        hotel[location[0]] = {}
        hotel[location[0]][location[1]] = occupant
    # Assume we don't have any check in issues and return True.
    # This will probably change.
    return True

def do_checkout(location):
    # This can be simplified.
    # We've handed of a lot of the room checks to the is_room_empty() function
    del hotel[location[0]][location[1]]
    return True

status = start_check_in_or_out()

if status == 'in':
    # We're going to setup a loop if a user isn't able to check in to a particular room.
    # If they can check in, they'll be done.
    # If not, we'll prompt for a new floor/room choice.
    checked_in = False
    while checked_in == False:
        location = get_room_and_floor()
        room_empty = is_room_empty(location[0], location[1])
        # Is the room empty? If so, check in!
        if room_empty == True:
            checked_in = do_checkin(location)
        else:
            # If not, let the user know and go back the start of this loop.
            print("That room is occupied, please choose another room.")
            checked_in = False

elif status == 'out':
    checked_out = False
    while checked_out == False:
        location = get_room_and_floor()
        # Are we checking out of an occupied room?
        room_empty = is_room_empty(location[0], location[1])
        if room_empty == True:
            # If the room isn't occupied, go back to the start of the loop.
            print("There isn't anyone in that room.")
            checked_out = False
        else:
            # Otherwise, try to check the user out
            checked_out = do_checkout(location)

print(hotel)
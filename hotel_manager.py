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

# Let's move the check in and check out process into a function.
def do_check_in_or_out():
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

# Let's clean up the redundancy with the floor and room checks.
def get_room_and_floor():
    # We're going to resume the best and assume a user inputs only numbers
    floor = int(input('Which floor would you prefer?'))
    room = int(input('Which room would you prefer?'))
    # Return the floor and then the room.
    # This will allow us to access them in the 0 and 1 index order
    return floor, room

status = do_check_in_or_out()

if status == 'in':
    # Run the new function to get the room and floor choices
    location = get_room_and_floor()
    occupant = input('What is your name?')
    # I'm going to purposely be verbose here.
    # This could be simplified into hotel[location[0]][location[1]]
    floor = location[0]
    room = location[1]
    hotel[floor][room] = occupant
elif status == 'out':
    location = get_room_and_floor()
    floor = location[0]
    room = location[1]
    del hotel[floor][room]

print(hotel)
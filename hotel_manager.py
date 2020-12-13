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

# Let's clean up the redundancy with the floor and room checks.
def get_room_and_floor():
    # We're going to resume the best and assume a user inputs only numbers
    floor = int(input('Which floor would you prefer?'))
    room = int(input('Which room would you prefer?'))
    # Return the floor and then the room.
    # This will allow us to access them in the 0 and 1 index order
    return floor, room

def do_checkin(location, people):
    # Does the chosen floor exist?
    # We can print the keys in the hotel dictionary to check.
    print(hotel.keys())
    if location[0] in hotel.keys():
        # If it exists, check in the user
        hotel[location[0]][location[1]] = occupant
    else:
        # If the floor doesn't exist we'll need to create it.
        # This prevents KeyError problems.
        hotel[location[0]] = {}
        hotel[location[0]][location[1]] = occupant

def do_checkout(location):
    # Let's make sure we're checking out from a room a floor that exists
    # At some point, we'll want to check the room exists too.
    if location[0] in hotel.keys():
        del hotel[location[0]][location[1]]
    else:
        print("That floor/room is not in this hotel.")
    # Right now, this will end the program,
    # we'll want to give the user a chance to go back and try a different room/floor


status = start_check_in_or_out()

if status == 'in':
    # Run the new function to get the room and floor choices
    location = get_room_and_floor()
    occupant = input('What is your name?')
    do_checkin(location, occupant)

elif status == 'out':
    location = get_room_and_floor()
    do_checkout(location)

print(hotel)
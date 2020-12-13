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

status = do_check_in_or_out()

if status == 'in':
    # We're going to assume best case scenario for checkin.
    # We'll check in one person, on an existing floor, into a new room.
    floor = int(input('Which floor would you prefer?'))
    room = int(input('Which room would you prefer?'))
    # We're going to start with a single occupant
    occupant = input('What is your name?')
    # Now add the room and occupant to the floor
    hotel[floor][room] = occupant
elif status == 'out':
    # We're going to assume best case scenario for checkout as well.
    # There is some redundancy here that we'll fix later.
    floor = int(input('What floor was your room on?'))
    room = int(input('What is your room number?'))
    del hotel[floor][room]


print(hotel)
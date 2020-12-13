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

# We'll kick off with a simply "in" or "out" response, and we'll make sure to conver it to lower
check_in_or_out = input("Are you checking in, or out?").lower()

# We'll start by assuming that a user always answers correctly. (Hint: They won't!)
if check_in_or_out == 'in':
    # We're going to assume best case scenario for checkin.
    # We'll check in one person, on an existing floor, into a new room.
    floor = int(input('Which floor would you prefer?'))
    room = int(input('Which room would you prefer?'))
    # We're going to start with a single occupant
    occupant = input('What is your name?')
    # Now add the room and occupant to the floor
    hotel[floor][room] = occupant
else:
    # We're going to assume best case scenario for checkout as well.
    # There is some redundancy here that we'll fix later.
    floor = int(input('What floor was your room on?'))
    room = int(input('What is your room number?'))
    del hotel[floor][room]

print(hotel)
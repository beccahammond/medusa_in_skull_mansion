#Rebecca Hammond

# Create the variables and functions we will need throughout the game
# Create a bool to keep track of whether the user won or lost yet
won_or_lost = False
# Add dictionary to link rooms to other rooms and the item in each room
rooms = {
        'Forehead Foyer': {'South': 'Head Hallway', 'West': 'Audio Atrium', 'East': 'Sonic Studio', 'Item': ''},
        'Audio Atrium': {'East': 'Forehead Foyer', 'Item': 'Poison Plant'},
        'Sonic Studio': {'West': 'Forehead Foyer', 'Item': 'Short Sword'},
        'Head Hallway': {'North': 'Forehead Foyer', 'South': 'Mandible Megaron', 'Item': 'Cursed Mirror'},
        'Mandible Megaron': {'North': 'Head Hallway', 'South': 'Skull Sauna', 'Item': 'Artistic Album'},
        'Skull Sauna': {'North': 'Mandible Megaron', 'West': 'Cranial Cloakroom', 'East': 'Canine Crypt', 'Item': 'Towel'},
        'Cranial Cloakroom': {'East': 'Skull Sauna', 'Item': 'Cannibal Cloak'},
        'Canine Crypt': {'West': 'Skull Sauna', 'Item': ''},
}
# Set the current room to the foyer to start
current_room = 'Forehead Foyer'
# Create a list of items the user has picked up
items = []

#define a function to print the room and items each loop
def print_game_info():
    #always reference the global current_room
    global current_room
    # Announce which room the user is currently in
    print('You are in the', current_room)
    # Announce the items the user has picked up so far
    print('Inventory :', items)
    # Print any items the user can grab in the current room (if any)
    item_to_grab = rooms[current_room]['Item']
    if item_to_grab != '':
        print('You see a {}'.format(item_to_grab))
    print('---------------------------')

# Define a function to handle user input
def get_new_state(user_move):
    # Make sure the user input a valid command depending on the first word
    if user_move.startswith('go'):
        # parse the user input to get the direction they want
        direction_specified = user_move.replace('go', '').strip()
        if direction_specified == '':
            print('Invalid input!')
            return
        # Try to move between rooms or let the user know they can't go that direction
        navigate(direction_specified)
    elif user_move.startswith('get'):
        # parse the user input to get the item they want
        item_specified = user_move.replace('get', '').strip()
        if item_specified == '':
            print('Invalid input!')
            return
        # try to retrieve the item or print an error message
        retrieve_item(item_specified)
    else:
        print('Invalid input!')

# Define a function to navigate between rooms
def navigate(direction):
    # Reference the global variable current room, we want to change it everywhere
    global current_room
    # Reference the global win/lose bool
    global won_or_lost
    directions = ['North', 'South', 'East', 'West']
    if direction not in directions:
        print('Invalid input!')
        return
    # Get the valid directions for the current room
    room_directions = rooms[current_room]
    # Verify the user can go the direction specified from valid directions
    if direction not in room_directions.keys():
        # let the user know they can't go that direction and return back to the loop for another move
        print('You can’t go that way!')
        return
    # Look up the new room if it's valid
    new_room = room_directions[direction]
    # Set the current room global variable to the new room
    current_room = new_room

    # If the current room is the canine crypt, the items were not all collected and the user lost
    if current_room == 'Canine Crypt':
        print('You see Medusa!')
        print('CRACK!  BANG!  You are now frozen.  GAME OVER!')
        won_or_lost = True

# Define a function to retrieve items
def retrieve_item(item):
    # Reference the global variable current room
    global current_room
    # Reference the global win/lose bool
    global won_or_lost

    # Check if the user already has the item first
    if item in items:
        print('Can\'t get {}!  You already have it!'.format(item))
        return

    # Check if user input a correct item name
    valid_items = []
    for data in rooms.values():
        if data["Item"] != '':
            valid_items.append(data["Item"])
    if item not in valid_items:
        print('Invalid input!  {} is not an item!'.format(item))
        return

    # Check if the item is actually in the room they are in
    room_item = rooms[current_room]['Item']
    if room_item == item:
        # If the item in the room, add the item to the user's inventory
        items.append(item)
        # Remove the item from the room
        rooms[current_room]['Item'] = ''
        # Let the user know the item was retrieved
        print('{} retrieved!'.format(item))
        # Check if the user has won the game by collecting all the items
        if len(items) == 6:
            print('Congratulations! You have collected all items and defeated Medusa!')
            won_or_lost = True
    elif room_item == '':
        # If there are no items in the room, print a more helpful error message
        print('Can\'t get {}!  There are no items in the {}!'.format(item, current_room))
    else:
        # If the item is not in the room, print an error
        print('Can\'t get {}!  Is it in another room?'.format(item))

# Start the game by outputting the game information and instructions
print('Medusa in Skull Mansion Adventure Game\n')
print('Collect 6 items to win the game, or be frozen by Medusa.')
print('Move commands: go South, go North, go East, go West')
print('Add to Inventory: get \'item name\'\n')

# Define the loop that keeps accepting user input until they win or lose
while(won_or_lost != True):
    #print the current room and items
    print_game_info()
    # Prompt the user for their move and strip white space from the input
    user_move = input('Enter your move:\n').strip()
    # Get new game state by passing user input to a function
    get_new_state(user_move)

# When the user wins or loses the game, print an ending message
print('Thanks for playing the game. Hope you enjoyed it.')
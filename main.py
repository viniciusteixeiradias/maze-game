import os
# import getch  # Requires `pip install getch`

def display_maze(maze, player_pos):
    """Displays the current state of the maze with the player position."""
    os.system('cls' if os.name == 'nt' else 'clear')

    for y in range(len(maze)):
        row = ""
        for x in range(len(maze[y])):
            if (y, x) == player_pos:
                row += "P"  # Player position
            else:
                row += maze[y][x]
        print(row)

def move_player(player_pos, direction, maze):
    """Moves the player in the specified direction if possible."""
    y, x = player_pos
    if direction == "w" and y > 0 and maze[y - 1][x] != "#":  # Up
        return (y - 1, x)
    elif direction == "s" and y < len(maze) - 1 and maze[y + 1][x] != "#":  # Down
        return (y + 1, x)
    elif direction == "a" and x > 0 and maze[y][x - 1] != "#":  # Left
        return (y, x - 1)
    elif direction == "d" and x < len(maze[0]) - 1 and maze[y][x + 1] != "#":  # Right
        return (y, x + 1)
    return player_pos 

def play_maze_game():
    maze = [
        "####",
        "#P.#",
        "##.#",
        "#..E",

        # "###############",
        # "#.....#.......#",
        # "#.####.#.#####.#",
        # "#.....#.#.....#",
        # "###.#####.###.#",
        # "#.....#.......#",
        # "#.#####.#####.#",
        # "#.#.....#.....#",
        # "#.#.#######.#.#",
        # "#...#...#.....#",
        # "#####.###.#####",
        # "#.............E",
        # "###############"
    ]

    # Convert maze to list of lists for mutability
    maze = [list(row) for row in maze]
    
    # Starting player position
    player_pos = (1, 1)

    print("Welcome to Maze Adventure!")
    print("Navigate to the exit (E) using W (up), A (left), S (down), D (right) keys.")
    input("Press Enter to start...")

    # Main game loop
    while True:
        display_maze(maze, player_pos)
        
        # Check for victory condition
        if maze[player_pos[0]][player_pos[1]] == "E":
            print("Congratulations! You've reached the exit!")
            break

        # Get a single keystroke without pressing Enter
        # move = getch.getch().lower()  # Capture single key press and make lowercase

        move = input("Enter your move: ").lower()

        # Process the move if it's a valid direction
        if move in ["w", "a", "s", "d"]:
            player_pos = move_player(player_pos, move, maze)

# Start the game
play_maze_game()

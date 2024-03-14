import os

def move(position, data):
    """
    Move function to determine the row and position for placing symbol.
    
    Args:
    position (int): The position chosen by the player.
    data (str): The symbol to be placed (X or O).
    
    Returns:
    tuple: Tuple containing position, symbol, and row.
    """
    row1 = [1, 2, 3]
    row2 = [4, 5, 6]
    row3 = [7, 8, 9]
    if position in row1:
        return (position - 1, data, "row1")
    elif position in row2:
        return (position - 4, data, "row2")
    elif position in row3:
        return (position - 7, data, "row3")

def print_base():
    """Print the base of the Tic Tac Toe board."""
    print(row_1, row_2, row_3, sep="\n")

def add_data(data1):
    """
    Add data to the rows based on input.
    
    Args:
    data1 (tuple): Tuple containing position, symbol, and row.
    """
    if data1[2] == "row1":
        row_1[data1[0]] = turn[1]
    elif data1[2] == "row2":
        row_2[data1[0]] = turn[1]
    elif data1[2] == "row3":
        row_3[data1[0]] = turn[1]

def check(pos1):
    """
    Check the validity of input position.
    
    Args:
    pos1 (int): The position chosen by the player.
    
    Returns:
    bool: True if input is valid, False otherwise.
    """
    os.system('cls')
    if pos1 > 9:
        print("The input is too big. Please try again.")
        return False
    elif pos1 < 0:
        print("The input is too low. Please try again.")
        return False
    elif isinstance(pos1, str):
        print("The input is a string! Please provide a number.")
        return False
    else:
        return True

def check_win(ro1, ro2, ro3, data):
    """
    Check if there's a winner.
    
    Args:
    ro1 (list): First row.
    ro2 (list): Second row.
    ro3 (list): Third row.
    data (str): Symbol (X or O) to check for winning.
    
    Returns:
    bool: True if there's a winner, False otherwise.
    """
    if ro1[0] == data and ro2[0] == data and ro3[0] == data:
        return True
    elif ro1[1] == data and ro2[1] == data and ro3[1] == data:
        return True
    elif ro1[2] == data and ro2[2] == data and ro3[2] == data:
        return True
    elif ro1[0] == data and ro1[1] == data and ro1[2] == data:
        return True
    elif ro2[0] == data and ro2[1] == data and ro2[2] == data:
        return True
    elif ro3[0] == data and ro3[1] == data and ro3[2] == data:
        return True
    elif ro1[0] == data and ro2[1] == data and ro3[2] == data:
        return True
    elif ro1[2] == data and ro2[1] == data and ro3[0] == data:
        return True

# Introduction to the game
print("Welcome to Tic Tac Toe!")
print("Enter the position from 1 to 9 where you want to place your symbol")

# Variables
count = 0
p1_turns = [0, 2, 4, 6, 8]
p2_turns = [1, 3, 5, 7]
row_1 = [" ", " ", " "]
row_2 = [" ", " ", " "]
row_3 = [" ", " ", " "]
filled_cells_position =[]
# Main program

while True:
    if count in p1_turns:  # Player 1's turn
        print_base()
        pos = int(input("Player 1, it's your turn. Select the position to place your X: "))
        check_value = check(pos)
        if check_value:
            if pos not in filled_cells_position:
                filled_cells_position += [pos]
                turn = move(pos, "X")
                add_data(turn)
                if count in [4, 6, 8]:
                    win = check_win(row_1, row_2, row_3, "X")
                    if win:
                        print("Congratulations Player 1, you won!")
                        print_base()
                        break
                os.system('cls')
                count += 1
            else:
                print("space already ocupied try again")
                continue
        else:
            continue

    elif count in p2_turns:  # Player 2's turn
        print_base()
        pos = int(input("Player 2, it's your turn. Select the position to place your O: "))
        check_value = check(pos)
        if check_value:
            if pos not in filled_cells_position:
                filled_cells_position += [pos]
                turn = move(pos, "O")
                add_data(turn)
                if count in [5, 7]:
                    win = check_win(row_1, row_2, row_3, "O")
                    if win:
                        print("Congratulations Player 2, you won!")
                        print_base()
                        break
                os.system('cls')
                count += 1
            else:
                print("space already ocupied try again")
                continue
        else:
            continue

    elif count > 8:
        print("It's a tie!")
        break

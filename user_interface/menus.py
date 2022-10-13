import os

def print_rules():
    ''' Should print the rules to terminal '''
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Rules:\n========")

    F_start = open("./game_rules/start_game.txt", "r")
    print("\n",F_start.read())
    F_start.close

    F_win = open("./game_rules/win_game.txt", "r")
    print("\n",F_win.read())
    F_win.close
    
    F_end = open("./game_rules/end_game.txt", "r")
    print("\n",F_end.read())
    F_end.close

    F_stack = open("./game_rules/move_stack.txt", "r")
    print("\n",F_stack.read())
    F_stack.close

    F_count = open("./game_rules/count_points.txt", "r")
    print("\n",F_count.read())
    F_count.close

    print("\n\nGo back [Enter]\n> ", end="")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')

def print_toolbar():
    ''' Prints the toolbar to terminal '''
    print("[P]lace a piece\n[M]ove a stack\n[D]isplay stack\n[R]ead the rules\n[Q]uit (resign)")
    print("=================\n> ", end="")

def print_main_menu():
    ''' Prints the main menu to terminal '''
    print("\n\nWelcome to UppsalaGame!")
    print("=================")
    print("[S]tart a new game\n[R]ead the rules\n[Q]uit")
    print("> ", end="")

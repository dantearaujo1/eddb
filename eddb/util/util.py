import os
def clear_screen():
    print("\033c", end='')
def move_cursor(x,y):
    print(f"\033[{y};{x}H", end='')
def get_terminal_size():
    return os.get_terminal_size()

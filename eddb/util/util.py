import os
import json

def clear_screen():
    print("\033c", end='')
def move_cursor(x,y):
    print(f"\033[{y};{x}H", end='')
def get_terminal_size():
    return os.get_terminal_size()

def open_json(file):
    with open(file, 'r') as f:
        dados = json.load(f)
        return dados

def load_data(file):
    with open_json(file) as data:
        print(data)


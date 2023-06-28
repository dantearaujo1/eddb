import uuid
import os
import json

def str_uuid4():
    return str(uuid.uuid4())

def clear_screen():
    print("\033c", end='')

def move_cursor(x,y):
    print(f"\033[{y};{x}H")

def get_terminal_size():
    return os.get_terminal_size()

def open_json(file):
    with open(file, 'r') as f:
        dados = json.load(f)
        return dados

def load_data(file):
    with open_json(file) as data:
        print(data)

def write_data(file,data):
    with open(file, 'w') as f:
        # pass
        # d = json.dumps(data)
        json.dump(data,f,indent=2,ensure_ascii=False)
    #     print()

def get_root(file):
    path = os.path.dirname(os.path.abspath(file))
    return path

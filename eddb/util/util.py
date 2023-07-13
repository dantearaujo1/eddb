from datetime import datetime,timezone
import time
import uuid
import os
import json

def str_uuid4():
    return str(uuid.uuid4())
def time_utc():
    return datetime.now(timezone.utc)

def clear_screen():
    print("\033c", end='')

def move_cursor(x,y):
    print(f"\033[{y};{x}H",end='', flush=True)

def set_terminal_size(row,column):
    print(f"\x1b[8;{row};{column}t",end="", flush=True)

def get_terminal_size():
    return os.get_terminal_size()

def open_json(filename):
    create_if_not_exist(filename)
    with open(filename, 'r') as f:
        try:
            dados = json.load(f)
            return dados
        except json.decoder.JSONDecodeError:
            return generate_database_structure()

def generate_database_structure():
    return {
        "books":[],
        "students":[],
        "loans":[],
    }

def create_if_not_exist(filename):
    if not os.path.isfile(filename):
        with open(filename, 'x'):
            print(f"Created file: {filename}")
            return True
    return False

def write_data(file,data):
    with open(file, 'w') as f:
        json.dump(data,f,indent=2,ensure_ascii=False)

def get_root(file):
    path = os.path.dirname(os.path.abspath(file))
    return path

# Isso vai ser nossa anotation para gerar rotas
# nas views
routes = {}
def route(action):
    def decorator(func):
        routes[action] = func
        return func
    return decorator

def handle_request(request_action,*parametros):
    for action, handler in routes.items():
        if action == request_action:
            return handler(*parametros)


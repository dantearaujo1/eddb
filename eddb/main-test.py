from readchar  import readkey, key
from eddb.util.util import move_cursor,clear_screen
def move(x,y):
    print(f"\033[{y};{x}H", end="", flush=True)
if __name__ == "__main__":
    pergunta = "Oi: "
    resposta = ''
    pos_x = len(pergunta) + len(resposta)
    while True:
        clear_screen()
        print(pergunta + resposta)
        # move_cursor(pos_x,0)
        k = readkey()
        if k == key.RIGHT:
            pos_x += 1
        elif k == key.LEFT:
            pos_x -= 1

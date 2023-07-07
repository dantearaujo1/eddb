import time
import random
import sys

from colorama import Back,Fore

from eddb.util.util import clear_screen,move_cursor,get_terminal_size


class EndView():
    def __init__(self):
        self.end = False
        self.colors = [Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.CYAN,Fore.WHITE,Fore.GREEN,Fore.YELLOW,Fore.RED,Fore.BLUE]

    def start(self):
        t = time.process_time()
        last = 0
        duration = 0.2
        changes = 10
        change_counter = 0
        counter = 0
        color = random.choice(self.colors)
        paint = True
        terminal_height = get_terminal_size()[1]
        while self.end is not True:
            t = time.process_time()
            delta = t - last
            counter += delta
            last = t
            if paint:
                clear_screen()
                move_cursor(1,terminal_height-3)
                print(f"{color}Até mais!")
                move_cursor(1,terminal_height-2)
                print(f"{color}Desenvolvido por:")
                move_cursor(1,terminal_height-1)
                print(f"{color}Dante e Débora")
                paint = False
            if counter > duration:
                change_counter += 1
                color = random.choice(self.colors)
                counter = 0
                paint = True
            if change_counter > changes:
                self.end = True
        sys.exit()

from colorama import Fore,Back,Style
from readchar import readkey, key
from eddb.util.util import clear_screen,get_terminal_size,move_cursor
from eddb.util.themes import get_theme

theme = get_theme("debora")

def draw_scrollable_menu(items,fake,ini_item):
    window_vertical_size = get_terminal_size()[1]
    window_horizontal_size = get_terminal_size()[0]
    fake_selected = fake
    end_item_position = window_vertical_size - 3 # 3 = Available Space
    menu_vertical_size = end_item_position
    total_items = len(items)
    padding = 1
    borders = {"right":theme["border_right"],"left":theme["border_left"],"up":theme["border_up"],"down":theme["border_down"]}
    clear_screen()
    move_cursor(0,window_vertical_size-total_items-2)
    if end_item_position < total_items and (ini_item + menu_vertical_size) < total_items - 1:
        print(f"{theme['scrollable_up_arrow_on']}^{Style.RESET_ALL}{(window_horizontal_size-4)*borders['up']}")
    else:
        print(f"{theme['scrollable_up_arrow_off']}^{Style.RESET_ALL}{(window_horizontal_size-4)*borders['up']}")

    for i in range(menu_vertical_size):
        if total_items > 0:
            if i // total_items > 0:
                break
            item = items[ini_item + i]
            move_cursor(0,window_vertical_size-i-2)
            if fake_selected == i:
                print(f"{padding*borders['left']}{theme['bselected']}{theme['fselected']}{item}")
            else:
                print(f"{padding*borders['left']}{item}")
    move_cursor(0,window_vertical_size-1)
    if ini_item > 0:
        print(f"{theme['scrollable_up_arrow_on']}v{Style.RESET_ALL}{(window_horizontal_size-4)*borders['down']}")
    else:
        print(f"{theme['scrollable_up_arrow_off']}v{Style.RESET_ALL}{(window_horizontal_size-4)*borders['down']}")



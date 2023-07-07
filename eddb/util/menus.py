from colorama import Fore,Back,Style
from readchar import readkey, key
from eddb.util.util import clear_screen,get_terminal_size,move_cursor
from eddb.util.themes import get_theme

theme = get_theme("debora")

def draw_scrollable_menu(items,fake,ini_item,reverse=False,other_lines=1):
    window_vertical_size = get_terminal_size()[1]
    window_horizontal_size = get_terminal_size()[0]
    fake_selected = fake
    end_item_position = window_vertical_size - 2 - other_lines# 3 = Available Space
    menu_vertical_size = end_item_position
    total_items = len(items)
    padding = 1
    borders = {"right":theme["border_right"],"left":theme["border_left"],"up":theme["border_up"],"down":theme["border_down"]}

    clear_screen()
    move_cursor(0,window_vertical_size-total_items-2)
    if reverse:
        if ini_item > 0:
            print(f"{theme['scrollable_up_arrow_on']}^{Style.RESET_ALL}{(window_horizontal_size-4)*borders['up']}")
        else:
            print(f"{theme['scrollable_up_arrow_off']}^{Style.RESET_ALL}{(window_horizontal_size-4)*borders['up']}")

        for i in range(menu_vertical_size):
            if total_items > 0:
                if i // total_items > 0:
                    break
                item = items[ini_item+i]
                if fake_selected == i:
                    print(f"{padding*borders['left']}{theme['bselected']}{theme['fselected']}{item}")
                else:
                    print(f"{padding*borders['left']}{item}")
        move_cursor(0,window_vertical_size-1)
        if (ini_item + menu_vertical_size) < total_items:
            print(f"{theme['scrollable_up_arrow_on']}v{Style.RESET_ALL}{(window_horizontal_size-4)*borders['down']}")
        else:
            print(f"{theme['scrollable_up_arrow_off']}v{Style.RESET_ALL}{(window_horizontal_size-4)*borders['down']}")
    else:
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



# def draw_scrollable_menu2(items,data_selection,u):
#     window_vertical_size = get_terminal_size()[1]
#     window_horizontal_size = get_terminal_size()[0]
#     fake_selected = fake
#     end_item_position = window_vertical_size - 3 # 3 = Available Space
#     menu_vertical_size = end_item_position
#     total_items = len(items)
#     padding = 1
#     borders = {"right":theme["border_right"],"left":theme["border_left"],"up":theme["border_up"],"down":theme["border_down"]}
#     clear_screen()
#     move_cursor(0,window_vertical_size-total_items-2)
#     if end_item_position < total_items and (ini_item + menu_vertical_size) < total_items - 1:
#         print(f"{theme['scrollable_up_arrow_on']}^{Style.RESET_ALL}{(window_horizontal_size-4)*borders['up']}")
#     else:
#         print(f"{theme['scrollable_up_arrow_off']}^{Style.RESET_ALL}{(window_horizontal_size-4)*borders['up']}")
#
#     for i in range(menu_vertical_size):
#         if total_items > 0:
#             if i // total_items > 0:
#                 break
#             item = items[ini_item + i]
#             move_cursor(0,window_vertical_size-i-2)
#             if fake_selected == i:
#                 print(f"{padding*borders['left']}{theme['bselected']}{theme['fselected']}{item}")
#             else:
#                 print(f"{padding*borders['left']}{item}")
#     move_cursor(0,window_vertical_size-1)
#     if ini_item > 0:
#         print(f"{theme['scrollable_up_arrow_on']}v{Style.RESET_ALL}{(window_horizontal_size-4)*borders['down']}")
#     else:
#         print(f"{theme['scrollable_up_arrow_off']}v{Style.RESET_ALL}{(window_horizontal_size-4)*borders['down']}")
#
#     k = readkey()
#     if k  == key.ENTER:
#         pass
#     if k in (key.CTRL_N,key.CTRL_J,key.DOWN):
#         selected -= 1
#         if fake_selection > 0:
#             fake_selection -=1
#         else:
#             if end_item > window:
#                 ini_item -= 1
#                 end_item -= 1
#     elif k in (key.CTRL_P,key.CTRL_K,key.UP):
#         selected += 1
#         if fake_selection < window - 1:
#             fake_selection +=1
#         else:
#             if ini_item < total - window - 1:
#                 ini_item += 1
#                 end_item += 1
#     elif k in (key.BACKSPACE):
#         anwser = anwser[0:-1]
#         ini_item = 0
#         end_item = window
#         fake_selection = 0
#         search = True
#     else:
#         anwser += k
#         ini_item = 0
#         end_item = window
#         fake_selection = 0
#         search = True

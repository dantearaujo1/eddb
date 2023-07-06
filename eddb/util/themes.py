from colorama import Back,Fore

themes = {
    "dante":{
        "scrollable_up_arrow_on":Back.BLUE,
        "scrollable_up_arrow_off":Back.LIGHTBLACK_EX,
        "bselected":Back.WHITE,
        "fselected":Fore.BLACK,
        "border_left":"|",
        "border_right":"|",
        "border_up":"*",
        "border_down":"*",
        "bloan_active":Back.GREEN,
        "floan_active":Fore.BLACK,
        "bloan_inactive":Back.LIGHTBLACK_EX,
        "floan_inactive":Fore.WHITE,
        "bloan_overdue":Back.RED,
        "floan_overdue":Fore.WHITE,
    },
    "debora":{
        "scrollable_up_arrow_on":Back.CYAN,
        "scrollable_up_arrow_off":Back.RED,
        "bselected":Back.BLACK,
        "fselected":Fore.BLUE,
        "border_left":"|",
        "border_right":"|",
        "border_up":"*",
        "border_down":"*",
        "bloan_active":Back.GREEN,
        "floan_active":Fore.BLACK,
        "bloan_inactive":Back.LIGHTBLACK_EX,
        "floan_inactive":Fore.WHITE,
        "bloan_overdue":Back.RED,
        "floan_overdue":Fore.WHITE,
    }
}

def get_theme(name:str):
    return themes[name]

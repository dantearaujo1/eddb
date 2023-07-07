from readchar import readkey, key

from eddb.util.util import clear_screen

class Menu():

    def __init__(self,data=None,size=[10,10]):
        self.selection = 0
        self.__data = data
        self.__size = size

    def set_data(self,data):
        self.__data = data

    def set_size(self,size):
        self.__size = size

    def __next(self):
        if self.selection < len(self.__data) - 1:
            self.selection += 1

    def __previous(self):
        if self.selection > 0:
            self.selection -= 1

    def __select(self):
        return self.selection

    def show(self):
        clear_screen()

    def get_input(self):
        k = readkey()
        if k  == key.ENTER:
            self.__select()
        if k  == key.SPACE:
            clear_screen()
        if k in (key.CTRL_N,key.CTRL_J,key.DOWN):
            self.__next()
        elif k in (key.CTRL_P,key.CTRL_K,key.UP):
            self.__previous()
        return False



from os import system
from colorama import init
from eddb.util.util import clear_screen,set_terminal_size


init(autoreset=True)
def main():

    from eddb.book.book_composer import BookComposer
    from eddb.student.student_composer import StudentComposer
    from eddb.loan.loan_composer import LoanComposer
    from eddb.mainmenu.main_menu_composer import MainMenuComposer
    from eddb.endview.end_composer import EndComposer

    v = MainMenuComposer.create()
    set_terminal_size(10,30)
    try:
        v.start()
    except KeyboardInterrupt:
        clear_screen()
        EndComposer.create().start()

if __name__ == "__main__":
    main()

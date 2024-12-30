from curses import wrapper
from typing_test import TypingTest

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the typing test")
    stdscr.addstr("\nPress any key to continue!")

    while True:
        typingTest = TypingTest(stdscr)
        stdscr.getkey()
        typingTest.testWPM()
        stdscr.addstr(
            3,
            0, 
            "Congractulations! You have completed the test! Press any key to Continue..."
        )
        stdscr.nodelay(False)
        key = stdscr.getkey()

        # Check if the key is a single charecter before using ord()
        if isinstance(key, str) and len(key) == 1:
            if ord(key) == 27: # ASCII Value for Escape
                break

if __name__ == "__main__":
    wrapper(main)
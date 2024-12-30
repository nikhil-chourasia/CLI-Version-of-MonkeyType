import curses
import random
import time

class TypingTest:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.toTypeText = self.getLineToType()
        self.userTypedText = []
        self.wpm = 0
        self.startTime = time.time()

        # Initialising Color Pairs:
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)


    def getLineToType(self):
        with open("typing_texts.txt", "r",  encoding="utf-8") as file:
            lines = file.readlines()

        return random.choice(lines).strip()


    def displayWPM(self):
        self.stdscr.addstr(1, 0, f"WPM: {self.wpm}", curses.color_pair(3))
    

    def displayAccuracy(self):
        self.stdscr.addstr(
            2, 
            0, 
            f"Accuracy: {self.testAccuracy()}%",
            curses.color_pair(3),
        )


    def displayTypedChars(self):
        for i, char in enumerate(self.userTypedText):
            correctCharecter = self.toTypeText[i]
            # Using Color pair 1 if correct otherwise 2 if incorrect
            color = 1 if char == correctCharecter else 2
            self.stdscr.addstr(0, i, char, curses.color_pair(color))


    def displayDetails(self):
        self.stdscr.addstr(self.toTypeText)
        self.displayWPM()
        self.displayAccuracy()
        self.displayTypedChars()


    def testAccuracy(self):
        totalCharecters = min(len(self.userTypedText), len(self.toTypeText))
        # If there are no typed chars we will show accuracy 0
        if totalCharecters == 0:
            return 0.0
        
        matchingCharecters = 0

        for currentChar, targetChar in zip(self.userTypedText, self.toTypeText):
            if currentChar == targetChar:
                matchingCharecters += 1

        matchingPercentage = (matchingCharecters/totalCharecters) * 100
        return matchingPercentage


    def testWPM(self):
        self.stdscr.nodelay(True)

        while True:

            timeElapsed = max(time.time() - self.startTime, 1)

            self.wpm = round(len(self.userTypedText)/(timeElapsed/60) /5)
            self.stdscr.clear()
            self.displayDetails()
            self.stdscr.refresh()

            # Exit the loop when the user types in the total length of the text.
            if len(self.userTypedText) == len(self.toTypeText):
                self.stdscr.nodelay(False)
                break
            
            try:
                key = self.stdscr.getkey()
            except Exception:
                continue

            if isinstance(key, str) and len(key) == 1:
                if ord(key) == 27:
                    break

            if not self.userTypedText:
                self.startTime = time.time()

            if key in ("KEY_BACKSPACE", "\b", "\x7f"):
                if len(self.userTypedText) > 0:
                    self.userTypedText.pop()

            elif len(self.userTypedText) < len(self.toTypeText):
                self.userTypedText.append(key)

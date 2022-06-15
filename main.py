from curses import wrapper
import curses
from time import time

def start(stdscr):
    stdscr.clear()
    stdscr.addstr(0,0, "Hello Welcome To Typing Speed Test!!")
    stdscr.addstr(1,0, "Press any Key except ESC to Start.....")
    stdscr.refresh()
    stdscr.getkey()

def end(stdscr, wpm):
    stdscr.clear()
    stdscr.addstr(f"Your Word Per Minute cont is :{wpm}")
    stdscr.addstr(1,0,"Press any Key except ESC to continue....")
    stdscr.refresh()
    return stdscr.getkey()

def display(stdscr, target, current, wpm = 0):
    stdscr.clear()
    stdscr.addstr(target)
    for i,char in enumerate(current):
        correct_char = target[i]
        if correct_char == char:
            color = curses.color_pair(2)
        else:
            color = curses.color_pair(1)
        stdscr.addstr(0,i,char, color)
    stdscr.addstr(1,0, f"WPM : {wpm}")
    stdscr.refresh()

def Target_text(stdscr):
    target_text = "Hello this program is going to test your typing speed, It is a random text"
    words = target_text.split()
    avg_word_len = round(sum([len(w) for w in words])/len(words))
    current = []
    wpm = 0
    start_time = time()
    stdscr.nodelay(True)
    while True:
        time_passed = max(time() - start_time,1)
        wpm = round((len(current) * 60 / time_passed)/avg_word_len)

        display(stdscr, target_text, current, wpm)

        if ''.join(current) == target_text:
            break
        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in ('KEY_BACKSPACE','\b','\x08'):
            if len(current) > 0:
                current.pop()
        
        elif len(current) < len(target_text):
            current.append(key)
    stdscr.nodelay(False)
    return wpm
    

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    inp = 'a'
    while ord(inp) != 27:
        start(stdscr)
        wpm = Target_text(stdscr)
        inp = end(stdscr,wpm)


wrapper(main)
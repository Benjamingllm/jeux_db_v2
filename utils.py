
from blessed import Terminal
import time


term = Terminal()
def wait(seconds,hotkey,**args):
    end = time.time() + seconds
    while True:
        remaining = end - time.time()
        if remaining  <= 0:
            break
        with term.cbreak():
            k = term.inkey(timeout=remaining)

        action = hotkey.get(k) or hotkey.get(k.name)
        if action:
            action(**args)
            return          

def clear_screen():
    print("\033[H\033[2J\033[3J")

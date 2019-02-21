import keyboard
import time

# Usage: main.py  <delay> <filenames>

def main(filenames, delay):
    print("running autotyper, abort by pressing F6")
    for filename in filenames:
        print("reading %s" % (filename))
        with open(filename, "r") as file_handle:
            for chars in file_handle.read():
                if keyboard.is_pressed("f6"):
                    print("user aborted")
                    break
                keyboard.write(chars, delay)

if __name__ == "__main__":
    print("Starting autotyper in 5s")
    time.sleep(5)
    import sys
    delay = float(sys.argv[1])
    filenames = sys.argv[2:]
    sys.exit(main(filenames, delay))

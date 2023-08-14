import time

def print_typing(text, delay=0.015):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print('\n')
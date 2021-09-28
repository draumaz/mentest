import pygame, os

def config(ndl):
    if ndl == 0:
        return "save.txt" # This is what you want your save to be called...
    elif ndl == 1:
        return 20 # ...this is how many lines you want it to contain (it starts from 0!)...
    elif ndl == 2:
        return 0 # ...and this is what you want to fill each line with.
def exists():
    if not (os.path.exists(config(0))): # If the file doesn't exist...
        open(config(0), "w+").write(config(1)*(str(config(2))+"\n")) # ...create it, and fill it using config values.

def read():
    return list(map(int, open(config(0), "r").readlines())) # Return the entire file as an array of integers.

def write(line, state):
    arr = read() # Retrieve the current states...
    f = open(config(0), "w") # ...open the file...
    for i in range(0, (config(1))): # ...set loop ranges....
        if i == line:
            f.write(str(state)+"\n") # ...if the loop matches line, write state...
            continue
        f.write(str(arr[i])+"\n") # ...and write to the file!

def text_colors(active_sel):
    white = (255,255,255)
    green = (50,205,50)
    black = (000,000,000)
    if active_sel == 0:
        return (white,white)
    elif active_sel == 1:
        return (white,green)
    elif active_sel == 2:
        return (green,white)
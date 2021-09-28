import pygame, os

def config(ndl):
    if ndl == 0:
        return "save.txt"
    elif ndl == 1:
        return 20
    elif ndl == 2:
        return 0
        
def exists():
    if not (os.path.exists(config(0))):
        open(config(0), "w+").write(config(1)*(str(config(2))+"\n"))

def read():
    return list(map(int, open(config(0), "r").readlines()))

def write(line, state):
    arr = read()
    f = open(config(0), "w")
    for i in range(0, (config(1))):
        if i == line:
            f.write(str(state)+"\n")
            continue
        f.write(str(arr[i])+"\n")

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
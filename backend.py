import os, pygame, time

def screen_fade(screen, orig, dest, sleep_time, reverse):
    for i in range(orig, dest): #TODO find out if this is expensive
        if reverse == False:
            screen.fill((i,i,i))
        else:
            v = dest-i
            screen.fill((v,v,v))
        time.sleep(sleep_time)
        pygame.display.flip()

def screen_clear(screen, color):
    screen.fill((color))
    pygame.display.flip()

def config(ndl): # Savesys
    if ndl == 0:
        return "save.txt"
    elif ndl == 1:
        return 20
    elif ndl == 2:
        return 0

def exists(): # Savesys
    if not (os.path.exists(config(0))):
        open(config(0), "w+").write(config(1)*(str(config(2))+"\n"))

def read(): # Savesys
    return list(map(int, open(config(0), "r").readlines()))

def write(line, state): # Savesys
    arr = read()
    f = open(config(0), "w")
    for i in range(0, (config(1))):
        if i == line:
            f.write(str(state)+"\n")
            continue
        f.write(str(arr[i])+"\n")

def text_colors(active_sel): # Return active colors from selector
    white = (255,255,255)
    green = (50,205,50)
    black = (000,000,000)
    if active_sel == 0:
        return (white,white)
    elif active_sel == 1:
        return (white,green)
    elif active_sel == 2:
        return (green,white)
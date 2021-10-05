import os, pygame, time


def screen_fade(screen, orig, dest, sleep_time, reverse):
    for i in range(orig, dest):  # TODO find out if this is expensive
        if not reverse:
            screen.fill((i, i, i))
        else:
            v = dest - i
            screen.fill((v, v, v))
        time.sleep(sleep_time)
        pygame.display.flip()


def screen_clear(screen, color):
    screen.fill((color))
    pygame.display.flip()


def text_colors(active_sel):  # Return active colors from selector
    white = (255, 255, 255)
    green = (50, 205, 50)
    if active_sel == 0:
        return white, white
    elif active_sel == 1:
        return green, white
    elif active_sel == 2:
        return white, green


def text_colors_trip(active_sel):  # Return active colors from selector
    white = (255, 255, 255)
    green = (50, 205, 50)
    if active_sel == 0:
        return white, white, white
    elif active_sel == 1:
        return green, white, white
    elif active_sel == 2:
        return white, green, white
    elif active_sel == 3:
        return white, white, green


class savesys:
    def config(ndl):  # Savesys
        if ndl == 0:
            return "save.txt"
        elif ndl == 1:
            return 20
        elif ndl == 2:
            return 0

    def exists():  # Savesys
        if not (os.path.exists(savesys.config(0))):
            open(savesys.config(0), "w+").write(savesys.config(1) * (str(savesys.config(2)) + "\n"))

    def read():  # Savesys
        return list(map(int, open(savesys.config(0), "r").readlines()))

    def write(line, state):  # Savesys
        arr = savesys.read()
        f = open(savesys.config(0), "w")
        for i in range(0, (savesys.config(1))):
            if i == line:
                f.write(str(state) + "\n")
                continue
            f.write(str(arr[i]) + "\n")

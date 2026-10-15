import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

# ---------------- settings ----------------
SIZE = 100            # grid is SIZE x SIZE (lower it, e.g. 60, if it runs slowly)
FILL = 0.25           # fraction of cells alive at the start
INTERVAL_MS = 30      # delay between generations
AGE_CAP = 40          # age at which a cell reaches its brightest colour
CMAP = "magma"        # try: "viridis", "plasma", "turbo", "inferno"
# ------------------------------------------

# setup
grid = np.zeros((SIZE, SIZE), dtype=int)
new_grid = np.zeros_like(grid)
age = np.zeros((SIZE, SIZE), dtype=int)      # how long each cell has been alive (for colour)
trail = np.zeros((SIZE, SIZE))               # fading glow where cells died
generation = 0
paused = False


def reseed():
    global grid, age, trail, generation
    for r in range(SIZE):
        for c in range(SIZE):
            grid[r][c] = 1 if random.random() < FILL else 0
    age[:] = 0
    trail[:] = 0
    generation = 0


reseed()


def make_picture():
    # alive cells: colour by age, dead cells: faint fading glow
    age_part = 0.35 + 0.65 * np.minimum(age, AGE_CAP) / AGE_CAP
    glow_part = trail * 0.3
    return np.where(grid == 1, age_part, glow_part)


fig, ax = plt.subplots(figsize=(8, 8))
fig.patch.set_facecolor("black")
ax.set_axis_off()
image = ax.imshow(make_picture(), cmap=CMAP, vmin=0, vmax=1, interpolation="nearest")
title = ax.set_title("", color="white")


def update(frame):
    # this function is one pass of your old while-loop body;
    # FuncAnimation calls it again and again until you close the window
    global grid, new_grid, age, trail, generation

    if not paused:
        neighbour_list = []
        # neighbour check
        for row in range(SIZE):
            for col in range(SIZE):
                cell_state = grid[row][col]
                above_row = row - 1
                below_row = row + 1
                # now all we need do is move by column
                for i in range(3):
                    neighbour_column = col - 1 + i       # left, same, right of this cell
                    neighbour_list.append(int(grid[above_row % SIZE][neighbour_column % SIZE]))
                    neighbour_list.append(int(grid[row % SIZE][neighbour_column % SIZE]))
                    neighbour_list.append(int(grid[below_row % SIZE][neighbour_column % SIZE]))
                neighbour_list.pop(4)
                dead_neighbour_count = 0
                for i in range(len(neighbour_list)):
                    if neighbour_list[i] == 0:
                        dead_neighbour_count += 1
                # Rule application
                if cell_state == 1:
                    if dead_neighbour_count > 6 or dead_neighbour_count < 5:
                        new_grid[row][col] = 0
                    else:
                        new_grid[row][col] = 1
                elif cell_state == 0:
                    if dead_neighbour_count == 5:
                        new_grid[row][col] = 1
                    else:
                        new_grid[row][col] = 0
                # Reset
                neighbour_list = []
                dead_neighbour_count = 0

        # only copy once the whole generation is finished
        grid = new_grid.copy()

        # bookkeeping for the colours
        age = np.where(grid == 1, age + 1, 0)
        trail = np.where(grid == 1, 1.0, trail * 0.85)
        generation += 1
        if not grid.any():
            reseed()   # everything died, start again so it never stops by itself

    image.set_data(make_picture())
    title.set_text(f"Generation {generation}   |   alive: {int(grid.sum())}"
                   f"   |   space = pause, r = reseed")
    return image, title


def on_key(event):
    global paused
    if event.key == " ":
        paused = not paused
    elif event.key == "r":
        reseed()


fig.canvas.mpl_connect("key_press_event", on_key)

# count() gives endless frames, so it runs until you close the window
anim = FuncAnimation(fig, update, frames=count(), interval=INTERVAL_MS,
                     blit=False, cache_frame_data=False)
plt.show()
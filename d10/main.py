import sys
sys.setrecursionlimit(100000)  # Change 1500 to an appropriate value

import matplotlib.pyplot as plt
class ColoredGrid:
    def __init__(self, width, height, default_color='white'):
        self.width = width
        self.height = height
        self.default_color = default_color
        self.grid = [[default_color for _ in range(width)] for _ in range(height)]

    def update_cell(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = color

    def draw_grid(self):
        cell_size = 1.0

        fig, ax = plt.subplots()

        for i in range(self.height):
            for j in range(self.width):
                cell_color = self.grid[i][j]
                rect = plt.Rectangle((j * cell_size, i * cell_size), cell_size, cell_size, facecolor=cell_color, edgecolor='black')
                ax.add_patch(rect)

        ax.set_xlim(0, self.width)  # Set x-axis limits based on grid size
        ax.set_ylim(0, self.height)  # Set y-axis limits based on grid size
        ax.set_aspect('equal', 'box')
        ax.axis('off')
        plt.show()

hey = ColoredGrid(140, 140)

pipes = {
    '|': (0, 2),
    '-': (1, 3),
    'L': (0, 1),
    'J': (0, 3),
    '7': (2, 3),
    'F': (1, 2),
    '.': (-2, -2),
    'S': (-1, -1),
}


loop_pipes = []
def find_loop(grid, original_start, start, fr=None):
    global hey
    hey.update_cell(start[0], start[1], 'red')
    if (len(loop_pipes) > 900):
        hey.draw_grid()


    print(f"ON {start}, loop_pipes size: {len(loop_pipes)}")
    if fr is not None and start == original_start:
        return
    else:
        loop_pipes.append(start)
    st = grid[start[0]][start[1]]
    start_list: list[int] = list(start)
    if st.this[0] == 0:
        new_fr = 0
        if fr != 2:
            start_list[0] -= 1
            print(f"will go {st.this[0]}")
        else:
            other = st.this[1]
            new_fr = other
            print(f"no can't go {st.this[0]}, will go {other}")
            if other == 0:
                start_list[0] -= 1
            elif other == 1:
                start_list[1] += 1
            elif other == 2:
                start_list[0] += 1
            elif other == 3:
                start_list[1] -= 1
        find_loop(grid, original_start, tuple(start_list), new_fr)
    elif st.this[0] == 1:
        new_fr = 1
        if fr != 3:
            start_list[1] += 1
            print(f"will go {st.this[0]}")
        else:
            other = st.this[1]
            new_fr = other
            print(f"no can't go {st.this[0]}, will go {other}")
            if other == 0:
                start_list[0] -= 1
            elif other == 1:
                start_list[1] += 1
            elif other == 2:
                start_list[0] += 1
            elif other == 3:
                start_list[1] -= 1

        find_loop(grid, original_start, tuple(start_list), new_fr)
    elif st.this[0] == 2:
        new_fr = 2
        if fr != 0:
            start_list[0] += 1
            print(f"will go {st.this[0]}")
        else:
            other = st.this[1]
            new_fr = other
            print(f"no can't go {st.this[0]}, will go {other}")
            if other == 0:
                start_list[0] -= 1
            elif other == 1:
                start_list[1] += 1
            elif other == 2:
                start_list[0] += 1
            elif other == 3:
                start_list[1] -= 1
        find_loop(grid, original_start, tuple(start_list), new_fr)
    elif st.this[0] == 3:
        new_fr = 3
        if fr != 1:
            start_list[1] -= 1
            print(f"will go {st.this[0]}")
        else:
            other = st.this[1]
            new_fr = other
            print(f"no can't go {st.this[0]}, will go {other}")
            if other == 0:
                start_list[0] -= 1
            elif other == 1:
                start_list[1] += 1
            elif other == 2:
                start_list[0] += 1
            elif other == 3:
                start_list[1] -= 1
        find_loop(grid, original_start, tuple(start_list), new_fr)

class Pipe:
    def __init__(self, this):
        self.this = this
        self.steps = -1


input = "input.txt"
f = open(input, "r")
lines = f.readlines()

print(f"ALSKDHJKLA {len(lines)} {len(lines[0])}")

grid = []
start: tuple
for line in lines:
    row = []
    for ch in line.strip():
        row.append(Pipe(pipes[ch]))
        if ch == 'S':
            start = (lines.index(line), line.strip().index(ch))
            row[len(row)-1].steps = 0
            # 🙄
            if input == "input.txt":
                row[len(row) - 1].this = (0,2)
            elif input == "test.txt":
                row[len(row) - 1].this = (1, 2)
    grid.append(row)
find_loop(grid, list(start), list(start))
print(loop_pipes)
print(f"max steps: {float(len(loop_pipes))/2}")

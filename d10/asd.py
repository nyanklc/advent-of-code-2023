import matplotlib.pyplot as plt


# Example usage
width = 5
height = 5
default_color = 'white'
colored_grid = ColoredGrid(width, height, default_color)

# Update individual cells with specific colors
colored_grid.update_cell(1, 2, 'red')
colored_grid.update_cell(3, 3, 'green')
colored_grid.update_cell(2, 1, 'blue')

# Draw the current state of the grid
colored_grid.draw_grid()

# You can continue updating and redrawing the grid as needed
colored_grid.update_cell(0, 0, 'yellow')
colored_grid.update_cell(4, 4, 'purple')

# Draw the updated grid
colored_grid.draw_grid()

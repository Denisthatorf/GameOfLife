import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_test_task_grid():
    result = np.array(
        [[1,0,0,0,0,0,0],
        [0,0,1,0,0,1,1],
        [1,0,0,1,0,0,1],
        [0,1,1,0,1,1,0],
        [1,1,1,1,0,0,1],
        [1,1,1,1,1,1,1],
        [1,1,0,1,1,0,1]])
    return result
 
def count_neighbors(grid, size, x, y):
    total = 0 
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i,j) != (x, y) and i > -1 and j > -1 and i < size and j < size:
                total += grid[i,j]
    return total
                

def update(frameNum, img, grid, size):
 
    next = grid.copy()
    for x in range(size):
        for y in range(size):
            state = grid[x,y]
            neighbors = count_neighbors(grid, size, x, y)
            if not state and neighbors == 3:
               next[x, y] = True
            elif state and neighbors not in [2, 3]:
               next[x, y] = False
            else:
               next[x, y] = state
               
    img.set_data(next)
    grid[:] = next[:]
    return img,
 
def main():
 
    ##if you want rando matrix
    #random matrix N*N
    #size = 1000
    #grid =  np.random.randint(2, size=(size, size))

    size = 7
    grid = generate_test_task_grid()
 
    # set up animation
    interval = 500
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, size),
                                  frames = 10,
                                  interval=interval,
                                  save_count=50)
 
    plt.show()
 
# call main
if __name__ == '__main__':
    main()
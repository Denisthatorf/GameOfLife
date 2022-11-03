from gol import generate_test_task_grid, update

import numpy as np
import matplotlib.pyplot as plt

def main():
 
    ##if you want random matrix
    #random matrix N*N
    #size = 1000
    #grid =  np.random.randint(2, size=(size, size))

    size = 7
    grid = generate_test_task_grid()
 
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')

    step = input("Step = ")
    step = int(step)
    for i in range(step):
        update(0, img, grid, size)
 
    plt.show()
 
# call main
if __name__ == '__main__':
    main()
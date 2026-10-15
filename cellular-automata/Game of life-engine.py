import random
import numpy as np 
import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation 

#setup 
grid =np.zeros((4,4), dtype=int)
new_grid=np.zeros_like(grid)
grid[2][2]=1
grid[1][2]=1
grid[3][2]=1

n=True

neighbour_list =[]
while n=True:
# neighbour check 
    for row in range(4):
        for col in range(4):
            cell_state=grid[row][col]
            above_row=row-1
            below_row=row+1
            # now all we need do is move by column 
            for i in range(3):
                neighbour_list.append(int(grid[above_row%4][(col - 1 + i)%4]))
                neighbour_list.append(int(grid[row%4][(col - 1 + i)%4]))
                neighbour_list.append(int(grid[below_row%4][(col - 1 + i)%4]))
            neighbour_list.pop(4)
            dead_neighbour_count=0
            for i in range(len(neighbour_list)):
                if neighbour_list[i]==0:
                    dead_neighbour_count+=1
    #Rule application
            if cell_state==1: 
                if dead_neighbour_count>6 or dead_neighbour_count<5:
                    new_grid[row][col]=0
                else:
                    new_grid[row][col]=1
            elif cell_state==0:
                if dead_neighbour_count==5:
                    new_grid[row][col]=1
                else:
                    new_grid[row][col]=0
        #Reset
            neighbour_list=[]
            dead_neighbour_count=0
    grid = new_grid.copy()




            

           
                 



 


# Conway's Game of Life — Real-Time Python Simulation

An interactive implementation of Conway's Game of Life built from scratch using **Python**, **NumPy**, and **Matplotlib**. This project explores cellular automata dynamics, toroidal (wrap-around) boundary conditions, and real-time frame-by-frame rendering with custom visual aging effects.

## 🚀 Features
* **Custom Grid Engine:** Built from scratch using NumPy arrays with periodic/toroidal boundary handling.
* **Real-Time Animation:** Powered by `matplotlib.animation.FuncAnimation` combined with an infinite frame generator (`itertools.count`).
* **Visual Enhancements:** Features dynamic color-grading based on cell age and fading visual trails for dead cells using Matplotlib colormaps (e.g., `magma`)[cite: 1].
* **Interactive Controls:** 
  * Press **Spacebar** to **pause/resume** the simulation.
  * Press **r** to **reseed** the board with a fresh random distribution[cite: 1].

## 🛠️ Requirements
Make sure you have the required libraries installed:
```bash
pip install numpy matplotlib

## Run the simulation script from your terminal
python "Game of life simulation.py"

To close the simulation window, simply click the close button on the render frame.

import matplotlib.pyplot as plt
import numpy as np

def main():
    n = int(input("Enter the number of points: "))
    x_coords = []
    y_coords = []
    
    for i in range(n):
        x = float(input(f"Enter x-coordinate of point {i + 1}: "))
        y = float(input(f"Enter y-coordinate of point {i + 1}: "))
        x_coords.append(x)
        y_coords.append(y)
    
    colors = plt.cm.viridis(np.linspace(0, 1, n))
    
    plt.scatter(x_coords, y_coords, color=colors, edgecolor='k')
    for i in range(n - 1):
        plt.plot(x_coords[i:i + 2], y_coords[i:i + 2], color=colors[i])
    
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Graph for your data")
    plt.grid(True)
    
    plt.show()

if __name__ == "__main__":
    main()

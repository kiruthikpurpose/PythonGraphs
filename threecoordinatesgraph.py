import matplotlib.pyplot as plt
import numpy as np

def main():
    n = int(input("Enter the number of points: "))
    x_coords = []
    y_coords = []
    z_coords = []
    
    for i in range(n):
        x = float(input(f"Enter x-coordinate of point {i + 1}: "))
        y = float(input(f"Enter y-coordinate of point {i + 1}: "))
        z = float(input(f"Enter z-coordinate of point {i + 1}: "))
        x_coords.append(x)
        y_coords.append(y)
        z_coords.append(z)
    
    colors = plt.cm.viridis(np.linspace(0, 1, n))
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(x_coords, y_coords, z_coords, c=colors, edgecolor='k')
    
    for i in range(n - 1):
        ax.plot(x_coords[i:i + 2], y_coords[i:i + 2], z_coords[i:i + 2], color=colors[i])
    
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_title("Graph for your data")
    
    plt.show()

if __name__ == "__main__":
    main()

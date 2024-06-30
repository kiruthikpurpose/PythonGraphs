import matplotlib.pyplot as plt
import numpy as np

def main():
    n = int(input("Enter the number of terms: "))
    terms = []
    
    for i in range(n):
        term = float(input(f"Enter term {i + 1}: "))
        terms.append(term)
    
    x = np.arange(1, n + 1)
    colors = plt.cm.viridis(np.linspace(0, 1, n))
    
    plt.scatter(x, terms, color=colors, edgecolor='k')
    for i in range(n - 1):
        plt.plot(x[i:i + 2], terms[i:i + 2], color=colors[i])
    
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Graph for your data")
    plt.grid(True)
    
    plt.show()

if __name__ == "__main__":
    main()

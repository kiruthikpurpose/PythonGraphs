# Data Plotting with Matplotlib

This repository contains three Python scripts for generating visualizations using `matplotlib` and `numpy`. Each script takes input for either 1D, 2D, or 3D data and visualizes them in interactive plots. The scripts are named based on the type of data they handle: `OneCoordinateGraph.py`, `TwoCoordinatesGraph.py`, and `ThreeCoordinatesGraph.py`.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [OneCoordinateGraph.py](#onecoordinategraphpy)
  - [TwoCoordinatesGraph.py](#twocoordinatesgraphpy)
  - [ThreeCoordinatesGraph.py](#threecoordinatesgraphpy)
- [License](#license)

## Requirements

- Python 3.x
- `matplotlib`
- `numpy`

You can install the required libraries using pip:

```bash
pip install matplotlib numpy
```

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/kiruthikpurpose/PythonGraphs.git
    cd PythonGraphs
    ```

2. Ensure you have Python 3.x installed on your system.

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### OneCoordinateGraph.py

This script allows you to plot a series of values (`n` terms) against their index positions (1D data).

To run the script:

```bash
python OneCoordinateGraph.py
```

You will be prompted to enter the number of terms and the values themselves. The script will display a scatter plot with lines connecting consecutive terms, with colors applied based on their index.

### TwoCoordinatesGraph.py

This script generates a 2D scatter plot based on `n` pairs of (x, y) coordinates.

To run the script:

```bash
python TwoCoordinatesGraph.py
```

After entering the number of points and their x, y coordinates, the script will display a 2D plot with each point connected to the next, with a color gradient based on their order.

### ThreeCoordinatesGraph.py

This script allows you to plot `n` points in 3D space using their (x, y, z) coordinates.

To run the script:

```bash
python ThreeCoordinatesGraph.py
```

You will be prompted to input the number of points followed by their respective x, y, and z coordinates. The script will generate a 3D scatter plot, connecting consecutive points and using a color gradient for clarity.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

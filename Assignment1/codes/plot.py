import matplotlib.pyplot as plt

def plot_points_with_labels_and_save_as_png(points, labels, filename='plot.png'):
    """
    Plot three points connected by lines, label each point with a given name, and save the plot as a PNG file.

    Parameters:
    points : List of tuples
        Each tuple contains the coordinates of a point (x, y).
    labels : List of strings
        Each string is the label for the corresponding point.
    filename : str
        The name of the file to save the plot as PNG.
    """
    if len(points) != len(labels):
        raise ValueError("The number of points must match the number of labels.")
    
    # Unzip the points into separate x and y coordinates
    x_coords, y_coords = zip(*points)
    
    # Create a plot
    plt.figure(figsize=(8, 6))
    
    # Plot the points and connect them with lines
    plt.plot(x_coords, y_coords, 'o-', color='blue', markersize=8, label='Points and Lines')
    
    # Annotate each point with its label
    for (x, y), label in zip(points, labels):
        plt.text(x, y, label, fontsize=12, ha='right', color='red')
    
    # Set labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Plot of Points Connected by Lines with Labels')
    plt.legend()
    plt.grid(True)
    
    # Save the plot as a PNG file
    plt.savefig(filename)
    plt.close()

# Example usage:
points = [(1, -5), (-3/2, 0), (-4, 5)]  # List of three points
labels = ['A(1,-5)', 'X(-3/2,0)', 'B(-4,5)']  # Labels for the points
plot_points_with_labels_and_save_as_png(points, labels, 'threeptgraph.png')

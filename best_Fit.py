import numpy as np
import matplotlib.pyplot as plt

def best_fit_line(x, y, order):
    # Fit a polynomial of the specified order
    coefficients = np.polyfit(x, y, order)

    # Create a polynomial function using the coefficients
    poly_function = np.poly1d(coefficients)

    return poly_function

def plot_best_fit_line(x, y, poly_function):
    # Plot the data points
    plt.scatter(x, y, label='Data Points')

    # Generate x values for the best fit line
    x_fit = np.linspace(min(x), max(x), 100)

    # Plot the best fit line
    plt.plot(x_fit, poly_function(x_fit), 'r', label=f'Best Fit Line (Order {len(poly_function)-1})')

    # Add labels and legend
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()

    # Show the plot
    plt.show()

# Example usage
if __name__ == "__main__":
    # Sample data points
    x_data = np.array([1, 2, 3, 4, 5])
    y_data = np.array([2, 3, 2.5, 4, 3.5])

    # Specify the order of the polynomial (e.g., 1 for linear, 2 for quadratic, etc.)
    
    polynomial_order = int(input())

    # Find the best-fit line of the given order
    poly_function = best_fit_line(x_data, y_data, polynomial_order)

    # Print the coefficients of the polynomial
    print(f"Coefficients of the best-fit line: {poly_function.coefficients}")

    # Plot the best-fit line along with data points
    plot_best_fit_line(x_data, y_data, poly_function)

import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [200, 220, 250, 300, 320, 280, 330, 310, 290, 280, 260, 240]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Data visualization tool function
def visualize_sales(dataframe):
    # Plotting the sales data
    plt.figure(figsize=(10, 6))
    plt.plot(dataframe['Month'], dataframe['Sales'], marker='o', linestyle='-', color='b')

    # Adding labels and title
    plt.title('Monthly Sales Data')
    plt.xlabel('Month')
    plt.ylabel('Sales ($)')
    plt.grid(True)

    # Show the plot
    plt.show()

# Call the visualization function with the provided dataset
visualize_sales(df)

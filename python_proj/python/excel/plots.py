import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_distribution(excel_file_path, column_name):
    # Read data from Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file_path)

    # Extract the specified column for distribution plot
    data_column = df[column_name]

    # Create a distribution plot using seaborn
    plt.figure(figsize=(10, 6))
    sns.histplot(data_column, kde=True, color='skyblue')
    plt.title(f'Distribution Plot of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')

    # Show the plot
    plt.show()

# Example usage:
excel_file_path = 'C:/python_proj/python/excel/excel_file.xlsx'
column_name_to_visualize = 'Value'
visualize_distribution(excel_file_path, column_name_to_visualize)

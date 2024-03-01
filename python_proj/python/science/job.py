# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load sample job market data (replace with your own dataset)
# Assume the dataset has columns like 'Year', 'Job Title', 'Salary', 'Location', etc.
data = {
    'Year': [2020, 2020, 2021, 2021, 2022, 2022],
    'Job Title': ['Developer', 'Analyst', 'Developer', 'Analyst', 'Engineer', 'Manager'],
    'Salary': [70000, 60000, 75000, 65000, 80000, 90000],
    'Location': ['CityA', 'CityB', 'CityA', 'CityB', 'CityC', 'CityC']
}

df = pd.DataFrame(data)

# Function to analyze and visualize job market trends
def analyze_and_visualize_trends(dataframe):
    # Group data by year and job title, calculate average salary
    grouped_data = dataframe.groupby(['Year', 'Job Title']).mean().reset_index()

    # Plot trends for each job title
    plt.figure(figsize=(12, 8))
    for job_title in grouped_data['Job Title'].unique():
        job_data = grouped_data[grouped_data['Job Title'] == job_title]
        plt.plot(job_data['Year'], job_data['Salary'], label=job_title, marker='o')

    plt.title('Job Market Trends Over Time')
    plt.xlabel('Year')
    plt.ylabel('Average Salary')
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the analysis and visualization
analyze_and_visualize_trends(df)

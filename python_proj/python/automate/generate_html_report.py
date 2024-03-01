import pandas as pd
from jinja2 import Environment, FileSystemLoader

def generate_html_report(data_file, report_template, output_file):
    # Read data from CSV file using pandas
    data = pd.read_csv(data_file)

    # Load Jinja2 environment and template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(report_template)

    # Render the template with data
    rendered_content = template.render(data=data)

    # Write the HTML report to a file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(rendered_content)

if __name__ == "__main__":
    # Specify the data file, report template, and output file
    data_file = "input/data.csv"  # Replace with the actual path to your data file
    report_template = "templates/report_template.html"  # Replace with the path to your HTML template
    output_file = "output/report.html"

    # Create the HTML report
    generate_html_report(data_file, report_template, output_file)

    print(f"HTML report generated and saved to: {output_file}")

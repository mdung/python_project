import os
import json
from jinja2 import Template
from datetime import datetime

def create_html(json_file_path, output_folder):
    # Load JSON data with explicit encoding (e.g., 'utf-8')
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # HTML template using Jinja2
    template_str = """
 <!DOCTYPE html>
<html>
<head>
    {% block header %}
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ data.title }}</title>
    {% endblock %}

    {% block styles %}
        <style>
            table {
                font-family: Arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }

            th, td {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }

            th {
                background-color: #f2f2f2;
            }

            .title {
                font-size: 1.5em;
                font-weight: bold;
            }

            .url {
                color: blue;
            }
        </style>
    {% endblock %}
</head>
<body>
    {% block body %}
        <h2 class="title">{{ data.title }}</h2>
        <table>
            <tr>
                <th>Key</th>
                <th>Value</th>
            </tr>
            {% for key, value in data.items() %}
                <tr>
                    <td>{{ key }}</td>
                    <td>{% if key == 'title' %}
                            <p>{{ value }}</p>
                        {% elif key == 'url' %}
                            <a href="{{ value }}" target="_blank">{{ value }}</a>
                        {% elif key == 'Description' %}
                            <p>{{ value }}</p>
                        {% elif key == 'Photo' %}
                            <img src="{{ value }}" alt="Photo">
                        {% elif value is string %}
                            {{ value }}
                        {% elif value is iterable %}
                            <ul>
                                {% for item in value %}
                                    <li>{{ item }}</li>
                                {% endfor %}
                            </ul>
                        {% else %}
                            {{ value }}
                        {% endif %}
                    </td>
                </tr>
            {% endfor %}
        </table>
    {% endblock %}
</body>
</html>
    """

    template = Template(template_str)

    # Generate HTML content using the template
    html_content = template.render(title=data.get('title', 'JSON to HTML'), data=data)

    # Create output HTML file with explicit encoding (e.g., 'utf-8')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(json_file_path))[0]}_{timestamp}.html")
    with open(output_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print(f"HTML file created: {output_file_path}")

def process_json_files(folder_path, output_folder):
    # Check if the output folder exists, create it if not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Recursively process each JSON file in the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.json'):
                json_file_path = os.path.join(root, filename)
                create_html(json_file_path, output_folder)

if __name__ == "__main__":
    # Replace 'input_folder' with the path to your folder containing JSON files
    input_folder = 'output'

    # Replace 'output_folder' with the path where you want to save the generated HTML files
    output_folder = 'html'

    process_json_files(input_folder, output_folder)

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Sample Rich Content</title>
</head>
<body>

    <h1>Welcome to My Rich Content Page</h1>

    <p>This is a sample HTML file with rich content. You can customize it based on your needs.</p>

    <h2>Important Points:</h2>
    <ul>
        <li>This is an item in a bulleted list.</li>
        <li>Another item in the list.</li>
    </ul>

    <p>Here's an example table:</p>
    
    <table border="1">
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
        </tr>
        <tr>
            <td>Row 1, Cell 1</td>
            <td>Row 1, Cell 2</td>
        </tr>
        <tr>
            <td>Row 2, Cell 1</td>
            <td>Row 2, Cell 2</td>
        </tr>
    </table>

    <p>Feel free to modify this content according to your requirements.</p>

</body>
</html>
"""

# Save the HTML content to a file
file_path = 'sample_rich_content.html'
with open(file_path, 'w') as file:
    file.write(html_content)

print(f"Sample rich content saved to {file_path}")

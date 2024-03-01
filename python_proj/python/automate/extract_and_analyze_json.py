import json
import xml.etree.ElementTree as ET

def extract_and_analyze_json(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Perform data analysis on the JSON data
    # Replace this section with your specific analysis tasks
    print("Data Analysis for JSON:")
    print("Number of records:", len(data))
    print("Example Record:")
    print(data[0])

def extract_and_analyze_xml(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Perform data analysis on the XML data
    # Replace this section with your specific analysis tasks
    print("\nData Analysis for XML:")
    print("Number of records:", len(root))
    print("Example Record:")
    for record in root:
        print(record.tag, record.attrib)

def main():
    # Specify the path to the JSON and XML files
    json_file_path = 'input/ata.json'
    xml_file_path = 'output/data.xml'

    # Extract and analyze data from the JSON file
    extract_and_analyze_json(json_file_path)

    # Extract and analyze data from the XML file
    extract_and_analyze_xml(xml_file_path)

if __name__ == "__main__":
    main()

import pdfplumber

def extract_table_data_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        table_data = []
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            tables = page.extract_tables()

            for table in tables:
                for row in table:
                    table_data.append(row)

    return table_data

def write_to_file(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for row in data:
            file.write(', '.join(str(cell) for cell in row) + '\n')

if __name__ == "__main__":
    pdf_path = "D:/download_organized/PDFs/Giới thiệu dự án Lumière Boulevard.VHGP.pdf"  # Replace with the actual path to your PDF file
    extracted_table_data = extract_table_data_from_pdf(pdf_path)

    output_file = "output/extracted_data.txt"  # Adjust the file name and path as needed
    write_to_file(extracted_table_data, output_file)

    print(f"Data extracted from PDF and written to: {output_file}")

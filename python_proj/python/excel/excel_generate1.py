from openpyxl import Workbook

# Create a new workbook
wb = Workbook()

# Create a new sheet
sheet = wb.active

# Add some sample data
sheet['A1'] = 'Name'
sheet['B1'] = 'Age'
sheet['A2'] = 'John Doe'
sheet['B2'] = 30
sheet['A3'] = 'Jane Doe'
sheet['B3'] = 25

# Save the workbook to a specific path
source_excel_file = 'C:/python_proj/python/excel/workbook.xlsx'
wb.save(source_excel_file)

print(f"Excel file created at: {source_excel_file}")

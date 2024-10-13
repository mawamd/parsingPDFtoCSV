import pdfplumber
import pandas as pd

with pdfplumber.open("file.pdf") as pdf:
    first_page = pdf.pages[0]
    
    # If you're happy with the table detection from debug_tablefinder:
    table = first_page.extract_table({
        "horizontal_strategy": "lines",  # Adjust to match what worked in the debug
        "vertical_strategy": "lines",    # Can use 'lines', 'text', or 'explicit'
    })

# Convert the table to a pandas DataFrame for easier viewing
df = pd.DataFrame(table)
print(df)
df.to_csv('table.csv', index=False)

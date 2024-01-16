import pandas as pd

# Specify the path to your Excel file
excel_file_path = r'C:\Users\Lenovo\Desktop\Python\file1.xlsx'

# Read the Excel file into a DataFrame
try:
    df = pd.read_excel(excel_file_path)
    
        # Add a new column with string operations
    df['Column2'] ='_' + (df.index + 1).astype(str)

    # Write the result to a new Excel file
    df.to_excel(excel_file_path, index=False)
    
    # Display the contents of the DataFrame
    print("Contents of the Excel file:")
    print(df)
    
except FileNotFoundError:
    print(f"Error: The file '{excel_file_path}' was not found.")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{excel_file_path}' is empty.")
except pd.errors.ParserError:
    print(f"Error: Unable to parse the contents of the file '{excel_file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
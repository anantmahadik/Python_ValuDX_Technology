import pandas as pd

# Specify the path to your Excel file
excel_file_path = 'C:\Users\Lenovo\Desktop\Python\file1.xlsx'
excel_file_path2 = 'C:\Users\Lenovo\Desktop\Python\file2.xlsx'
excel_file_path_newfile = 'C:\Users\Lenovo\Desktop\Python\file5.xlsx'



# Read the Excel file into a DataFrame
try:
    # Read only the specified sheet
        df1 = pd.read_excel(excel_file_path)
        df2 = pd.read_excel(excel_file_path2)
        df3 = pd.dataFrame()
        

    
except FileNotFoundError:
    print(f"Error: The file '{excel_file_path}' was not found.")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{excel_file_path}' is empty.")
except pd.errors.ParserError:
    print(f"Error: Unable to parse the contents of the file '{excel_file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

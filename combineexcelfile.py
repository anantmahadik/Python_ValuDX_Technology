import pandas as pd

# Specify the paths to your Excel files
excel_file_path2 = r'C:\Users\Lenovo\Desktop\Python\file2.xlsx'
excel_file_path3 = r'C:\Users\Lenovo\Desktop\Python\file3.xlsx'
excel_file_path_combined = r'C:\Users\Lenovo\Desktop\Python\combined_file.xlsx'

try:
    # Read the necessary columns from the Excel files into DataFrames
    df2 = pd.read_excel(excel_file_path2, usecols=['Revenue'])
    df3 = pd.read_excel(excel_file_path3, usecols=['Region'])

    # Combine the selected columns into a new DataFrame
    df_combined = pd.concat([df2, df3], axis=1)

    # Display the contents of the combined DataFrame
    print("Contents of the combined DataFrame:")
    print(df_combined)

    # Write the result to a new Excel file
    df_combined.to_excel(excel_file_path_combined, index=False)

except FileNotFoundError as e:
    print(f"Error: {e}")
except pd.errors.EmptyDataError:
    print(f"Error: One of the files is empty.")
except pd.errors.ParserError as e:
    print(f"Error: Unable to parse the contents of a file. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
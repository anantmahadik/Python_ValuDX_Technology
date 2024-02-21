# Writing binary data to a file in wb mode
with open("valuedx_5.bin", "wb") as file:
    # Example binary data (bytes representing the ASCII values for "Hello World")
    binary_data = bytes([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100])

    # Write binary data to the file
    file.write(binary_data)

print("File closed:", file.closed)

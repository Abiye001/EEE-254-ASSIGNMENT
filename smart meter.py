# Step 1: Open the file for reading
fh = open("meter_readings.txt", "r")  # Opens file for reading

# Step 2: Read all lines (each line is a meter reading)
lines = fh_readlines(fh)  # Returns a list of strings, e.g., ["150.5", "162.3", "175.8", "180.2"]

# Step 3: Process the readings (convert to floats and calculate average)
readings = [float(line) for line in lines]  # Convert each string to float
average = sum(readings) / len(readings)  # Calculate average: (150.5 + 162.3 + 175.8 + 180.2) / 4 = 167.2

# Step 4: Close the file
fh_close(fh)  # Closes the file

# Step 5: Open the file again in append mode to add a new reading
fh = append("meter_readings.txt", "a")  # Opens file for appending

# Step 6: Write a new meter reading to the file
new_reading = "190.5"
fh_write(fh, new_reading + "\n")  # Writes "190.5" with a newline to the end of the file

# Step 7: Close the file
fh_close(fh)  # Closes the file

# Step 8: Create a new file to store the average
new_fh = fopen("average_reading.txt", "w")  # Opens a new file for writing

# Step 9: Write the average to the new file using fh_writelines (since it takes a sequence)
fh_writelines(new_fh, [str(average) + "\n"])  # Writes the average (e.g., "167.2") to the file

# Step 10: Close the new file
fh_close(new_fh)  # Closes the file

# Step 11: Read back the average file to confirm
confirm_fh = open("average_reading.txt", "r")  # Opens the average file for reading
content = fh_read(confirm_fh)  # Reads the entire content as a string, e.g., "167.2\n"
first_line = fh_readline(confirm_fh)  # Attempts to read the first line (but cursor is at the end, so likely empty)
fh_close(confirm_fh)  # Closes the file

# Print the results for verification
print(f"Average reading: {average}")
print(f"Content of average_reading.txt: {content}")
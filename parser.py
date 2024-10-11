import re
import matplotlib.pyplot as plt
import os

# Inform the user about the file location
print("Ensure the file you want to parse is in the same directory as 'parser.py'.")

# Prompt the user for input
file_name = input("Enter the name of the file to parse: ")
string_to_parse = input("Enter the string portion to identify (e.g., 'length=' or 'l='): ")
output_file_name = input("Enter the name for the output .txt file: ")
graph_file_name = input("Enter the name for the graph file (without extension): ")

# Construct the file path
file_path = os.path.join(os.getcwd(), file_name)

lengths = []

# Read and parse the file
with open(file_path, "r") as file:
    data = file.read()
    length_pattern = re.compile(rf'{re.escape(string_to_parse)}(\d+)')
    lengths = length_pattern.findall(data)
    lengths = [int(length) for length in lengths]

# Write lengths to a text file
with open(output_file_name, "w") as output_file:
    for length in lengths:
        output_file.write(f"{length}\n")

# Print smallest and largest lengths
smallest_length = min(lengths)
largest_length = max(lengths)
print(lengths)
print(f"Smallest length: {smallest_length}")
print(f"Largest length: {largest_length}")

# Prompt the user for axis titles
x_axis_title_line_plot = input("Enter the x-axis title for the line plot: ")
y_axis_title_line_plot = input("Enter the y-axis title for the line plot: ")
x_axis_title_histogram = input("Enter the x-axis title for the histogram: ")
y_axis_title_histogram = input("Enter the y-axis title for the histogram: ")

# Plotting
plt.figure(figsize=(10, 6))
graph_title = input("Enter the title for the graph: ")
plt.suptitle(graph_title)  # Add a title to the entire figure

# Line plot
plt.subplot(2, 1, 1)  # 2 rows, 1 column, 1st subplot
plt.plot(range(1, len(lengths) + 1), lengths, marker='o', linestyle='-')
plt.title('Gene Lengths')
plt.xlabel(x_axis_title_line_plot)  # Use user input for x-axis title
plt.ylabel(y_axis_title_line_plot)  # Use user input for y-axis title
plt.grid(True)

# Histogram
plt.subplot(2, 1, 2)  # 2 rows, 1 column, 2nd subplot
n, bins, patches = plt.hist(lengths, bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Gene Lengths')
plt.xlabel(x_axis_title_histogram)  # Use user input for x-axis title
plt.ylabel(y_axis_title_histogram)  # Use user input for y-axis title
plt.grid(True)

# Annotate each bin with its frequency
for i in range(len(patches)):
    plt.text(bins[i] + (bins[i+1] - bins[i]) / 2, n[i], str(int(n[i])), ha='center', va='bottom')

plt.tight_layout()

# Save the plot
plt.savefig(f"{graph_file_name}.png")
plt.close()  # Close the plot window after saving



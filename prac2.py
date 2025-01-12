# Import necessary libraries
import pandas as pd

# Step 1: Import the sales data from a CSV file
# Replace 'sales_data.csv' with the actual file path or name
input_file = "Superstore.csv"
Superstore = pd.read_csv(input_file)

# Display the first few rows of the data
print("Original Sales Data:")
print(Superstore.head())

# Step 2: Perform basic data cleaning
# Example: Fill missing values with 0 (or another suitable value)
Superstore.fillna(0, inplace=True)

# Example: Rename columns for consistency
Superstore.rename(columns={"Product": "Product Name", "Revenue": "Total Revenue"}, inplace=True)

# Step 3: Add a new column for sales tax
# Assume a sales tax rate of 10% (0.10)
sales_tax_rate = 0.10
Superstore["Sales Tax"] = Superstore["Total Revenue"] * sales_tax_rate

# Add a new column for total cost (Revenue + Sales Tax)
Superstore["Total Cost"] = Superstore["Total Revenue"] + Superstore["Sales Tax"]

# Display the modified data
print("\nModified Sales Data:")
print(Superstore.head())

# Step 4: Export the updated data to a new CSV file
# Replace 'updated_sales_data.csv' with the desired output file name
output_file = "Superstore2.csv"
Superstore.to_csv(output_file, index=False)

print(f"\nThe updated sales data has been saved to '{output_file}'.")

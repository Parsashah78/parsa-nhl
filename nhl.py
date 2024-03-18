import numpy as np
import matplotlib.pyplot as plt

# Sample data: monthly sales of a product for a year
sales_data = [100, 120, 130, 110, 150, 160, 200, 190, 180, 170, 160, 150]


total_sales = sum(sales_data)

# Calculate the average monthly sales
average_sales = np.mean(sales_data)

# Calculate the maximum and minimum sales months
max_sales = max(sales_data)
min_sales = min(sales_data)

# Find the month with the highest sales
max_month_index = sales_data.index(max_sales) + 1  # Adding 1 to start indexing from month 1
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
max_month = months[max_month_index - 1]  # Subtracting 1 to get the correct index in months list

# Plotting the sales data
plt.figure(figsize=(10, 6))
plt.plot(months, sales_data, marker='o', linestyle='-')
plt.title('Monthly Sales of a Product')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Annotate the maximum sales point
plt.annotate(f'Max: {max_sales}', xy=(max_month_index - 1, max_sales), xytext=(max_month_index - 1, max_sales + 10),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center')

# Show the plot
plt.show()

# Print the analysis results
print("Total sales for the year:", total_sales)
print("Average monthly sales:", average_sales)
print("Month with the highest sales:", max_month)
print("Maximum sales in a month:", max_sales)
print("Minimum sales in a month:", min_sales)
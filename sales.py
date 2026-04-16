import pandas as pd

# creating dicyionary that represents sales raw data
data = {
    "Date": [
        "2026-04-01", "2026-04-01", "2026-04-02",
        "2026-04-02", "2026-04-03", "2026-04-03"
    ],
    "Product": ["Milk", "Bread", "Eggs", "Butter", "Milk", "Eggs"],
    "Category": ["Dairy", "Bakery", "Dairy", "Dairy", "Dairy", "Dairy"],
    "Price": [3.5, 2.0, 4.0, 5.0, 3.5, 4.0],
    "Quantity": [10, 20, 15, 5, 8, 12]
}

# convert the dictionary into a DataFrame
df = pd.DataFrame(data)

#check 
# print(df)

# Save the dataFrame to a csv file to simulate a real-world dataset
df.to_csv("sales_data.csv", index=False) #prevents saving row numbers in the CSV

# Read the CSV file into a new DataFrame
sales_df = pd.read_csv("sales_data.csv")

# Display the first five rows
print(sales_df.head())

# Shows column names,  data types, and missig values
print(sales_df.info())

#Provides mean, min, max, etc
print(sales_df.describe())

# create a new column "revenue"
sales_df["Revenue"] = sales_df["Price"] * sales_df["Quantity"]

# Display the updates DataFrame
print(sales_df)

# Total revenue 
total_rev = sales_df["Revenue"].sum()
print(total_rev)

# best selling product
product_sales = sales_df.groupby("Product")["Quantity"].sum()
best_product = product_sales.sort_values(ascending=False)
print(best_product)

# Revenue by Category
category_revenue = sales_df.groupby("Category")["Revenue"].sum()
print(category_revenue)

# Average Price per Product
average_price = sales_df.groupby("Product")["Price"].mean()
print(average_price)
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
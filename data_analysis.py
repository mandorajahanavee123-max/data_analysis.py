# Import pandas
import pandas as pd

# Step 1: Load dataset (make sure CSV is in same folder)
df = pd.read_csv("books_data.csv")

# Step 2: Explore data
print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Statistical Summary ---")
print(df.describe())

# Step 3: Handle missing values
df = df.dropna()  # remove rows with missing values

# Step 4: Clean Price column (remove £ and convert to float)
df['Price'] = df['Price'].str.replace('£', '').astype(float)

# Step 5: Filter data (price > 50)
filtered_data = df[df['Price'] > 50]

print("\n--- Books with Price > 50 ---")
print(filtered_data)

# Step 6: Sort data by price (descending)
sorted_data = df.sort_values(by='Price', ascending=False)

print("\n--- Top Expensive Books ---")
print(sorted_data.head())

# Step 7: Group data by Rating
grouped_data = df.groupby('Rating')['Price'].mean()

print("\n--- Average Price by Rating ---")
print(grouped_data)

# Step 8: Add new column (Discount Price)
df['Discount_Price'] = df['Price'] * 0.9

print("\n--- Data with Discount Column ---")
print(df.head())

# Step 9: Export cleaned data
df.to_csv("cleaned_books_data.csv", index=False)

print("\nCleaned data saved successfully!")
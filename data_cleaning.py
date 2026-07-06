import pandas as pd
df = pd.read_excel("Dataset for Data Analytics.xlsx")

print("Original Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows Found: {duplicates}")

df = df.drop_duplicates()

df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

df["Date"] = pd.to_datetime(df["Date"])
df.to_excel("Cleaned_Dataset_Project1.xlsx", index=False)

print("\nData Cleaning Completed Successfully!")
print("Final Shape:", df.shape)
print("Cleaned dataset saved as Cleaned_Dataset_Project1.xlsx")
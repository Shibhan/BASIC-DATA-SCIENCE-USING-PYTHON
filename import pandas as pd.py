import pandas as pd

# Load the dataset
df =pd.read_csv('student-mat.csv')

# Display the first few rows
df.head()

# Check for missing values
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

# Display column data types
data_types = df.dtypes
print("\nData Types:\n", data_types)

# Understand the dataset's size
dataset_size = df.shape
print("\nDataset Size:\n", dataset_size)

# Handle missing values (if any)
# For this example, let's assume we replace missing values with the median
df.fillna(df.median(), inplace=True)

# Remove duplicate entries
df.drop_duplicates(inplace=True)

average_g3 = df['G3'].mean()
print(f"The average score in math (G3) is: {average_g3:.2f}")

students_above_15 = df[df['G3'] > 15].shape[0]
print(f"The number of students who scored above 15 in their final grade (G3) is: {students_above_15}")

correlation_studytime_g3 = df['studytime'].corr(df['G3'])
print(f"The correlation between study time and final grade (G3) is: {correlation_studytime_g3:.2f}")

average_g3_by_gender = df.groupby('sex')['G3'].mean()
print(f"Average final grade (G3) by gender:\n{average_g3_by_gender}")

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hist(df['G3'], bins=10, edgecolor='k', alpha=0.7)
plt.title('Histogram of Final Grades (G3)')
plt.xlabel('Final Grade (G3)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['studytime'], df['G3'], alpha=0.7)
plt.title('Scatter Plot of Study Time vs Final Grade (G3)')
plt.xlabel('Study Time (hours/week)')
plt.ylabel('Final Grade (G3)')
plt.grid(True)
plt.show()

average_g3_by_gender.plot(kind='bar', figsize=(10, 6), alpha=0.7, color=['blue', 'pink'])
plt.title('Average Final Grade (G3) by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Final Grade (G3)')
plt.xticks(rotation=0)
plt.grid(True)
plt.show()
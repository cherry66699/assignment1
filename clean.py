import pandas as pd

# Set the file paths
input1 = "C:/Users/22899/Desktop/econ7035/assignment1/respondent_contact.csv"
input2 = "C:/Users/22899/Desktop/econ7035/assignment1/respondent_other.csv"
output = "C:/Users/22899/Desktop/econ7035/assignment1/respondent_cleaned.csv"

# Step 1: Merge the two input data files based on the ID value
df1 = pd.read_csv(input1)
df2 = pd.read_csv(input2)
merged_df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')

# Drop the redundant column
merged_df.drop('id', axis=1, inplace=True)

# Step 2: Drop any rows with missing values
merged_df.dropna(inplace=True)

# Step 3: Drop any rows if their job value contains 'insurance' or 'Insurance'
merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]

# Step 4: Save the cleaned data to the output file
merged_df.to_csv(output, index=False)



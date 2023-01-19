import pandas as pd

# Read in the .CSV file
df = pd.read_csv("output.csv")

# Determine if Rural (Population >= 5,000)
for i in range(0, len(df["School"]) - 1):
    if (df["Population"][i] < 5000):
        df.loc[i, ["Is Rural"]] = [1]
    elif (df["Population"][i] >= 5000):
        df.loc[i, ["Is Rural"]] = [0]

# Drop the rows with NA/None
result = df.dropna(subset=["Is Rural", "Population", "Town", "2019"])

# Update the indices
result = result.reset_index()

# Calculate the change
for i in range(0, len(result) - 1):
    result.loc[i, "Change"] = result["2022"][i] - result["2019"][i]

# Compute the correlation

print(result.corr(method="pearson"))

print(result.describe())

result.to_csv("~/Desktop/Output.csv")
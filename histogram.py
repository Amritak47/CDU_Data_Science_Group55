import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame with group information and mean age values
data = {
    "Group": ["PPD Group", "Healthy Group"],
    "Mean Age": [64.86, 62.55],
    "Std Age": [8.97, 10.79]
}

# changing data into a pandas DataFrame
df = pd.DataFrame(data)

plt.figure(figsize=(8, 6))
plt.bar(df["Group"], df["Mean Age"], yerr=df["Std Age"], capsize=7, color=['blue', 'green'])
plt.title("Comparison of Mean Age between PPD and Healthy Groups")
plt.xlabel("Group")
plt.ylabel("Mean Age")
plt.ylim(0, max(df["Mean Age"]) + max(df["Std Age"]) + 5)


for index, row in df.iterrows():
    plt.text(index, row["Mean Age"] + 2, f"{row['Mean Age']:.2f}", ha="center")


plt.tight_layout()
plt.show()

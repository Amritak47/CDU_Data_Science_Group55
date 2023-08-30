
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


file_path = "po1_data.txt"  
column_names = [
    "Subject ID", "Jitter (%)", "Jitter (abs)", "Jitter (rap)", "Jitter (ppq5)",
    "Jitter (ddp)", "Shimmer (%)", "Shimmer (abs)", "Shimmer (apq3)", "Shimmer (apq5)",
    "Shimmer (apq11)", "Shimmer (dda)", "Harmonicity (NHR)", "Harmonicity (HNR)",
    "Pitch (median)", "Pitch (mean)", "Pitch (std)", "Pitch (min)", "Pitch (max)",
    "Number of pulses", "Number of periods", "Mean period", "Std deviation of period",
    "Fraction of unvoiced frames", "Number of voice breaks", "Degree of voice breaks",
    "UPDRS", "PD indicator"
]

data = pd.read_csv(file_path, sep=",", names=column_names)


print(data.head())

print(data.info())
print(data.describe())

# Check for missing values
missing_values = data.isnull().sum()
print(missing_values)

# Data Visualization
#0 healthy and 1 with PD
sns.histplot(data=data, x='Jitter (%)', hue='PD indicator', bins=20, kde=True)
plt.title("Jitter (%) Distribution by PD Indicator")
plt.xlabel("Jitter (%)")
plt.ylabel("Frequency")
plt.show()

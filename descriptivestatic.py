import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# loading the dataset into a pandas DataFrame with specified column names
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


# descriptive statistics for PD group
pd_group_stats = data[data['PD indicator'] == 1].describe()

# descriptive statistics for healthy group
healthy_group_stats = data[data['PD indicator'] == 0].describe()

# set display options to show all columns
pd.set_option('display.max_columns', None)

# display descriptive statistics for PD group
print("Descriptive Statistics for PD Group:")
print(pd_group_stats)

# for healthy group
print("\nDescriptive Statistics for Healthy Group:")
print(healthy_group_stats)




# ata = pd.read_csv('po1_data.txt', sep=',')

# # Filter data for PD group
# pd_group_data = data[data['PD indicator'] == 1]['Pitch (mean)']
# # Calculate mean and standard deviation for PD group
# mean_pitch_pd = pd_group_data.mean()
# std_pitch_pd = pd_group_data.std()

# # Filter data for Non-PD group
# non_pd_group_data = data[data['PD indicator'] == 0]['Pitch (mean)']
# # Calculate mean and standard deviation for Non-PD group
# mean_pitch_non_pd = non_pd_group_data.mean()
# std_pitch_non_pd = non_pd_group_data.std()

# print("Mean of 'Pitch (mean)' for PD group:", mean_pitch_pd)
# print("Standard Deviation of 'Pitch (mean)' for PD group:", std_pitch_pd)
# print("Mean of 'Pitch (mean)' for Non-PD group:", mean_pitch_non_pd)
# print("Standard Deviation of 'Pitch (mean)' for Non-PD group:", std_pitch_non_pd)

# we use this dataset to calculate CI of Pitch(mean)

import scipy.stats as stats
import pandas as pd


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

significant_variables = []
for variable in data.columns[1:-2]:  
    pd_group_data = data[data['PD indicator'] == 1][variable]
    healthy_group_data = data[data['PD indicator'] == 0][variable]

    # perform the appropriate statistical test , using t-test for normally distributed data
    
    t_statistic, p_value = stats.ttest_ind(pd_group_data, healthy_group_data, equal_var=False)
    
    # compare p-value with a significance level of 0.05
    if p_value < 0.05:
        significant_variables.append(variable)
        print(f"{variable}: p-value = {p_value:.4f} (significant)")
    else:
        print(f"{variable}: p-value = {p_value:.4f}")

print("\nVariables with Significant Differences:")
print(significant_variables)

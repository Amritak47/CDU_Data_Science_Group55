import matplotlib.pyplot as plt 
# we just plot 3 variable which we get from descriptive statistics

pd_means = [1.206312, 10.173285, 25.000000]

nonpd_means = [1.183479, 9.825798, 1.000000]

#  variable names
variables = ['Mean Shimmer (%)', 'Mean Harmonicity (HNR)', 'Mean UPDRS']

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(variables, pd_means, color='blue', label='Parkinson\'s Group')
plt.bar(variables, nonpd_means, color='orange', label='Healthy Group', alpha=0.5)

plt.xlabel('Variables')
plt.ylabel('Mean Values')
plt.title('Comparison of Mean Values between Parkinson\'s and Healthy Groups')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()

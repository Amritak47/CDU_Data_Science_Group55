import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('po1_data.csv', header=None)

data.columns = [
    'Subject identifier',
    'Jitter1',
    'Jitter2',
    'Jitter3',
    'Jitter4',
    'Jitter5',
    'Shimmer1',
    'Shimmer2',
    'Shimmer3',
    'Shimmer4',
    'Shimmer5',
    'Shimmer6', 
    'Harmonicity1',
    'Harmonicity2',
    'Harmonicity3',
    'Pitch1',
    'Pitch2',
    'Pitch3',
    'Pitch4',
    'Pitch5',
    'Pulse1',
    'Pulse2',
    'Pulse3',
    'Pulse4',
    'Voice1',
    'Voice2',
    'Voice3',
    'UPDRS',
    'PD indicator'
]


# List of columns to plot histograms for
columns_to_plot = ['Jitter1', 'Jitter2', 'Shimmer1', 'Shimmer2', 'Harmonicity1', 'Pitch1']

# Loop through columns and generate histograms
for column in columns_to_plot:
    sns.histplot(data=data[column], bins=20)
    plt.title(f'Histogram of {column}')
    plt.xlabel(f'{column} Value')
    plt.ylabel('Frequency')
    plt.show()

# Create scatter plots
sns.scatterplot(data=data, x='Jitter1', y='Shimmer1')
plt.title('Scatter Plot of Jitter vs Shimmer')
plt.show()
# List of columns you want to plot
columns_to_plot = ['Jitter', 'Shimmer', 'Harmonicity', 'Pitch', 'Pulse', 'Voice']

# Loop through columns and generate histograms
##for column in columns_to_plot:
 ##  sns.histplot(data=data[column], bins=20)
  ##  plt.title(f'Histogram of {column}')
  ##  plt.xlabel(f'{column} Value')
  ##  plt.ylabel('Frequency')
  ##  plt.show()

# Create scatter plots
 ## sns.scatterplot(data=data, x='Jitter1', y='Shimmer1')
## plt.title('Scatter Plot of Jitter vs Shimmer')
##plt.show()

# Create pair plot
# Create pair plots
##sns.pairplot(data=data[['Jitter1', 'Jitter2', 'Shimmer1', 'Shimmer2', 'Harmonicity1', 'Pitch1', 'Pulse1', 'Voice1']])
##plt.suptitle('Pair Plots')
##plt.show()




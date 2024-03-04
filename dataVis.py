import pandas as pd  # Importing the pandas library with alias 'pd'
import seaborn as sns  # Importing the seaborn library with alias 'sns'
import matplotlib.pyplot as plt  # Importing the pyplot module from matplotlib with alias 'plt'


# Read the CSV file into a pandas DataFrame
df = pd.read_csv('file.csv', names=['Title', 'Link', 'Wikidata ID', 'Birth Year', 'Noteworthiness'])


# Convert 'Birth Year' and 'Noteworthiness' columns to numeric
df['Birth Year'] = pd.to_numeric(df['Birth Year'], errors='coerce')  # Convert 'Birth Year' to numeric, handle errors as NaN
df['Noteworthiness'] = pd.to_numeric(df['Noteworthiness'], errors='coerce')  # Convert 'Noteworthiness' to numeric, handle errors as NaN


# Drop rows with NaN values in 'Birth Year' or 'Noteworthiness'
df = df.dropna(subset=['Birth Year', 'Noteworthiness'])  # Drop rows where 'Birth Year' or 'Noteworthiness' is NaN


# Plot scattergraph
plt.figure(figsize=(10, 6))  # Create a new figure with size 10x6 inches
sns.scatterplot(x='Birth Year', y='Noteworthiness', data=df, alpha=0.7)  # Create a scatter plot using 'Birth Year' and 'Noteworthiness'
plt.xlabel('Birth Year')  # Set the label for the x-axis
plt.ylabel('Noteworthiness')  # Set the label for the y-axis
plt.title('Birth Year vs Noteworthiness')  # Set the title of the plot
plt.tight_layout()  # Adjust subplot parameters to give specified padding
plt.show()  # Display the plot


# Plot piechart 
# Uncomment these lines to plot a pie chart
# occurances = df['Century'].value_counts()
# plt.pie(occurances, labels=['13th','14th','15th','16th','17th','18th','19th','20th'], autopct='%1.1f%%')
# plt.title('Proportion of burials by Century')


# Plot barchart
# Uncomment these lines to plot a bar chart
# sns.barplot(x='Century', y='Noteworthiness', data=df)
# plt.title('Noteworthiness by Century')

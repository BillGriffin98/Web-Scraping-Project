import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read the CSV file into a pandas DataFrame
df = pd.read_csv('file.csv', names=['Title', 'Link', 'Wikidata ID', 'Birth Year', 'Century', 'Noteworthiness'])


# Convert 'Birth Year' and 'Hyperlink Count' columns to numeric
df['Birth Year'] = pd.to_numeric(df['Birth Year'], errors='coerce')
df['Noteworthiness'] = pd.to_numeric(df['Noteworthiness'], errors='coerce')


# Drop rows with NaN values in 'Birth Year' or 'Hyperlink Count'
df = df.dropna(subset=['Birth Year', 'Noteworthiness'])

# Plot scattergraph
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Birth Year', y='Noteworthiness', data=df, alpha=0.7)
plt.xlabel('Birth Year')
plt.ylabel('Noteworthiness')
plt.title('Birth Year vs Noteworthiness')
plt.tight_layout()
plt.show()


# Plot piechart 
#plt.pie(occurances, labels=['13th','14th','15th','16th','17th','18th','19th','20th'], autopct='%1.1f%%')
#plt.title('Proportion of burials by Century')


# Plot barchart
#sns.barplot(x = 'Century',y = 'Noteworthiness',data = df)
#plt.title('Noteworthiness by Century')






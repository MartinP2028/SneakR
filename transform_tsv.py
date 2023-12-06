import pandas as pd
import json

# Load JSON data into a pandas DataFrame
with open('data.json', 'r') as file:
    data = json.load(file)

# Normalize the data
df = pd.json_normalize(data)

# Convert DataFrame to TSV and save it to a file
df.to_csv('data.tsv', sep='\t', index=False)

# Imports
import os
import pandas as pd

# Set paths for input and output files
input_path = os.path.join("Resources", "cities.csv")
output_path = os.path.join("dataframe.html")

cities_df = pd.read_csv(input_path)

cities_df.to_html(output_path, index=False)
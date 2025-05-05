# unemployment_plotter.py

import pandas as pd
import matplotlib.pyplot as plt

class UnemploymentDataPlotter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Load CSV data into a DataFrame and parse the DATE column."""
        self.df = pd.read_csv(self.file_path)
        self.df['DATE'] = pd.to_datetime(self.df['DATE'])
        if 'abc' not in self.df.columns:
            raise ValueError("Expected column 'abc' not found in the CSV.")
        self.df = self.df.dropna(subset=['abc'])

    def print_headers(self):
        """Print the column headers with their indices."""
        print("Column headers in the dataset:")
        for index, column_name in enumerate(self.df.columns):
            print(f"Index {index}: Column '{column_name}'")

    def plot_data(self):
        """Plot the unemployment rate over time."""
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['DATE'], self.df['abc'], label='Unemployment Rate', color='blue')
        plt.xlabel('Date')
        plt.ylabel('Unemployment Rate (%)')
        plt.title('National Unemployment Rate (abc) Since 1976')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

# main.py
from pathlib import Path
from assignment_16 import UnemploymentDataPlotter

if __name__ == "__main__":
    file_path = Path.cwd() /'abc.csv'  
    plotter = UnemploymentDataPlotter(file_path)
    plotter.load_data()
    plotter.print_headers()
    plotter.plot_data()

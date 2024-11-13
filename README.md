# Pandas-student_performance_analysis
This project analyzes student performance data to uncover trends affecting academic outcomes. Using  Pandas, I explored attributes like age, gender, study time, and extracurricular participation to understand their impact on final grades. The analysis involved data cleaning, grouping, and aggregation

**Features**

- Data Cleaning: Removed null values, corrected data types, and standardized entries.
- Aggregation and Grouping: Grouped data to analyze performance across different demographics.
- Visualization: Graphs and charts for insights like performance trends, distribution, and correlations.

**Prerequisites**

Before you begin, make sure you have the following installed:

- **Python 3.7 or higher**: This project is built with Python, so having Python installed is essential. [Download Python here](https://www.python.org/downloads/).

- **Pandas**: A library for data manipulation and analysis. Install it via pip if you haven't:
   ```bash
   pip install pandas
# Dataset
The dataset is available in the `data` folder and is provided as a CSV file.

- File : `data/student_data.csv`
  
Make sure that the `student_data_task_solution.py` script is in the same directory as the `student_data` folder.

# Running the Script in PyCharm

Open PyCharm create a new file (student_data_task_solution.py)  and load the project directory (student_data.csv) by either opening the folder directly or importing the project.

1. **Import the Dataset**
    -import pandas as pd

2. **Load the dataset into a pandas DataFrame**
    -df = pd.read_csv('student_data.csv')

3. **Display the rows of the dataset**
    -print(df)








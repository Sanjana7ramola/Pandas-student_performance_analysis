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

1. ** Open the Project in PyCharm**
  - Open PyCharm and create a new Python project
  - Import the project directory containing student_data_task_solution.py and the data folder.
  - Ensure that the student_data.csv file is in the data folder and is accessible to the script.
2. **Import the Dataset**
In your student_data_task_solution.py, the first step is to import the required library:
   -  import pandas as pd

2. **Load the dataset into a pandas DataFrame**
 Now, load the dataset into a Pandas DataFrame:
    - df = pd.read_csv('student_data.csv')

4. **Display the rows of the dataset**
 You can print the dataset to inspect its content:
    - print(df)
This will output the rows of the dataset, showing all the student attributes.

The student_data_task_solution.py file contains the Pandas solutions to analyze the dataset. These solutions solve various questions related to student performance

5. **Run the Script**
 There are two ways to run the script:

- From the Terminal: Open the terminal within PyCharm or any terminal, navigate to the folder containing student_data_task_solution.py, and run:
   - python student_data_task_solution.py
- Using PyCharm’s Run Button: Simply click the Run button at the top of the IDE, or use the shortcut Shift + F10 to execute the script directly.

6. **6. View the Results**

The script will display output in the terminal.




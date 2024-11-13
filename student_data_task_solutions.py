import pandas as pd

df = pd.read_csv('student_data.csv')
print(df)

# Task 1: Filter students who are 18 years old and live in urban areas (address = 'U').
t1 =  (df[(df['age'] == 18) & (df['address'] == 'U')])
print(t1)

# Task 2: Filter female students (sex = 'F') who have more than 10 absences.
t2 =(df[(df['sex']=='F') & (df['absences']>10)])
print(t2)

# Task 3: Calculate the average grade (G3) of students.
t3 =(df['G3'].mean())
print(t3)

# Task 4: Find the maximum number of absences in the dataset.
t4 =(df['absences'].max())
print(t4)

# Task 5: Group the data by sex and calculate the average final grade (G3) for male and female students.
t5 = (df.groupby('sex')['G3'].mean())
print(t5)

# Task 6: Group by school and get the total number of absences per school.
t6 = (df.groupby('school')['absences'].sum())
print(t6)

# Task 7: Filter students who have both low workday alcohol consumption (Dalc <= 2) and high weekend alcohol consumption
# (Walc >= 4).
t7 =(df[(df['Dalc']<= 2)& df['Walc']>= 4])
print(t7)

# Task 8: Filter students whose parents both work as teachers (Mjob and Fjob = 'teacher').
t8 = (df[(df['Mjob']=='teacher') & (df['Fjob']=='teacher')])
print(t8)

# Task 9: Select students who are from large families (famsize = 'GT3') and have an above-average family relationship
# rating (famrel > 3).
t9=(df[(df['famsize']=='GT3') & (df['famrel']>3)])
print(t9)

# Task 10: Calculate the median final grade (G3) for students who have more than 5 absences.
t10 = df[df['absences'] > 5]['G3'].median()
print(t10)

# Task 11: Find the student with the highest grade (G3) who lives in rural areas (address = 'R').
t11 = (df[df['address'] == 'R']['G3'].max())
print(t11)

# Task 12: Compute the average grades (G3) of students who have at least one parent with a higher education level (Medu or Fedu >= 4).
filtering =df[(df['Medu']>=4) | (df['Fedu']>=4)]
t12 = (filtering['G3'].mean())
print(t12)

# Task 13: Group students by their family size (famsize) and calculate the average number of absences for each group.
t13 = df.groupby('famsize')['absences'].mean()
print(t13)

# Task 14: Group by both family relationship rating (famrel) and weekend alcohol consumption (Walc), and count the number
# of students in each group.
group = df.groupby(['famrel','Walc'])
t14 =  (group.size())
print(t14)

# Task 15: Group by sex and school, and compute the average final grade (G3) for each combination.
grping = df.groupby(['sex','school'])
t15 = (grping['G3'].mean())
print(t15)

# Task 16: For students older than 16 years, group by sex and calculate the maximum number of absences for each gender.
t16 = df[df['age'] > 16].groupby('sex')['absences'].max()
print(t16)

# Task 17: Filter students whose final grade (G3) is below the overall average, then group by their school and calculate
# the average absences for each school
overall_avg_g3 = df['G3'].mean()
below_avg_students = df[df['G3'] < overall_avg_g3]
t17 = below_avg_students.groupby('school')['absences'].mean()
print(t17)


# Task 18: Filter students who have excellent health (health = 5) and group by their address and school,
# then find the total number of students in each combination.
health_students =df[df['health'] == 5]
t18=(health_students.groupby(['address','school']).size())
print(t18)

# Task 19: Create a new column that calculates the average of the three grades (G1, G2, G3) for each student, and then
# find the top 5 students with the highest averages.
df['average'] = df[['G1', 'G2', 'G3']].mean(axis=1)
t19 = df.nlargest(5, 'average')
print(t19)

# Task 20: Create a custom function to categorize students into different groups based on their
# final grade (G3): 'Failing'(<10),'Passing' (>=10 and <15), and 'Excellent' (>=15). Apply this function and
# calculate the number of students in each group.
def grade_category(g):
    if g < 10:
        return 'Failing'
    elif g < 15:
        return 'Passing'
    else:
        return 'Excellent'

df['grade_category'] = df['G3'].apply(grade_category)
t20 = df['grade_category'].value_counts()
print(t20)

# Task 21 : Calculate the average final grade (G3) for students participating in extracurricular activities
# (activities = 'yes') and compare it with students who do not participate to evaluate its potential benefits
t21 =df.groupby('activities')['G3'].mean()
print(t21)

# Task 22 :Categorize students into "Pass" (G3 >= 10) and "Fail" (G3 < 10) groups, then calculate the pass rate for
# each level of family relationship quality (famrel).
df['pass_status'] = df['G3'].apply(lambda x: 'Pass' if x >= 10 else 'Fail')
t22 = df[df['pass_status'] == 'Pass'].groupby('famrel').size() / df.groupby('famrel').size() * 100
print(t22)

# Task 23 :Calculate the average progression in grades from G1 to G3 for each student and determine if there is an
# overall improvement trend across the class
t23 = (df['G3'] - df['G1']).mean()
print(t23)

# Task 24 :  Define "high alcohol consumption" as students who score 4 or above in both workday (Dalc) and
# weekend (Walc) alcohol consumption. Calculate the percentage of such students.
t24_high_alcohol_consumption = len(df[(df['Dalc'] >= 4) & (df['Walc'] >= 4)]) / len(df) * 100
print(t24_high_alcohol_consumption)


# Task 25 : Create age groups (e.g., 15-16, 17-18, 19-20) and calculate the cumulative number of absences for each age
# group to understand the attendance patterns of different age groups.
# Task 25: Create age groups (e.g., 15-16, 17-18, 19-20) and calculate the cumulative number of absences for each age group.
age_groups = pd.cut(df['age'], bins=[15, 17, 19, 21], labels=['15-16', '17-18', '19-20'])
t25 = df.groupby(age_groups, observed=False)['absences'].sum()
print(t25)






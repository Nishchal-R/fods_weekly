'''
Description of program:
This program demonstrates various data analysis and transformation operations on a sample employee dataset using Pandas.
Given a structured table of employee information, the program performs the following tasks:

a. Selects only the Name and Salary columns.
b. Filters out employees who work in the "IT" department.
c. Retrieves employees older than 30 and calculates the average salary for each department.
d. Counts the number of employees in each department.
e. Adds a new column "Bonus" representing 10% of the employee's salary.
f. Replaces all occurrences of "HR" in the Department column with "Human Resources."
g. Identifies the employee(s) with the longest tenure based on JoinDate.
h. Creates a "SalaryCategory" column classifying salaries as "High" if above 75,000 and "Low" otherwise.
i. Checks for and removes duplicate EmployeeIDs.
j. Calculates the median age of all employees.

This script illustrates the use of filtering, grouping, aggregation, conditional logic, string replacement, date operations, and duplicate handling in Pandas.
'''



import pandas as pd

# Sample employee data
data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['John Smith', 'Alice Brown', 'Bob White', 'Emma Green', 'Charlie Red'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'Age': [30, 28, 35, 40, 25],
    'Salary': [70000, 60000, 80000, 90000, 55000],
    'JoinDate': ['2018-07-15', '2020-03-10', '2016-11-01', '2012-05-25', '2021-06-01'],
    'ExperienceYears': [5, 3, 7, 11, 2]
}

# Create DataFrame
df = pd.DataFrame(data)

# (a)Select only Name and Salary columns
print("\n(a) Name and Salary columns:")
print(df[['Name', 'Salary']])

# (b)Filter out all employees in the "IT" department
print("\n(b) Employees NOT in IT Department:")
df_filtered = df[df['Department'] != 'IT']
print(df_filtered)

# (c)Employees older than 30
print("\n(c) Employees older than 30:")
older_than_30 = df[df['Age'] > 30]
print(older_than_30)

# and average salary by department
print("\nAverage salary by department:")
average_salary = df.groupby('Department')['Salary'].mean()
print(average_salary)

# (d)Count the number of employees in each department
print("\n(d) Number of employees in each department:")
print(df['Department'].value_counts())

# (e)Bonus column (10% of salary)
df['Bonus'] = df['Salary'] * 0.10
print("\n(e) Bonus column added:")
print(df[['Name', 'Salary', 'Bonus']])

# (f)Replace "HR" with "Human Resources"
df['Department'] = df['Department'].replace('HR', 'Human Resources')
print("\n(f) Updated Departments (HR -> Human Resources):")
print(df[['Name', 'Department']])

# (g)Employee(s) with the longest tenure
df['JoinDate'] = pd.to_datetime(df['JoinDate'])
longest_tenure = df[df['JoinDate'] == df['JoinDate'].min()]
print("\n(g) Employee(s) with longest tenure:")
print(longest_tenure)

# (h)SalaryCategory column
df['SalaryCategory'] = df['Salary'].apply(lambda x: 'High' if x > 75000 else 'Low')
print("\n(h) Salary Category (High if >75000):")
print(df[['Name', 'Salary', 'SalaryCategory']])

# (i)Remove duplicate EmployeeIDs
df_no_duplicates = df.drop_duplicates(subset='EmployeeID')
print("\n(i) Data after removing duplicates (if any):")
print(df_no_duplicates)

# (j)Median age
median_age = df['Age'].median()
print(f"\n(j) Median Age of employees: {median_age}")
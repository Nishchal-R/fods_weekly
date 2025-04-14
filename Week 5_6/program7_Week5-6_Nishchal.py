'''Write a program to implement a class called employee with attributes such as empid, name, address, contact_number, spouse 
name, number_of_child, salary. Instantiate this class to input the values for multiple employees and write it in a file “employees.csv”. 
Allow the user of your program to see the list of employees and their details as well. Try to use the concept of try/except too in the program.'''

import csv

# Define the Employee class with required attributes
class Employee:
    def __init__(self, empid, name, address, contact, spouse, children, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact = contact
        self.spouse = spouse
        self.children = children
        self.salary = salary

    # Convert employee data to a list for writing to CSV
    def to_list(self):
        return [self.empid, self.name, self.address, self.contact, self.spouse, self.children, self.salary]

# Function to write employee data to a CSV file
def save_employees(employees):
    try:
        with open("employees.csv", "w", newline='') as file:
            writer = csv.writer(file)
            # Write header row
            writer.writerow(["EmpID", "Name", "Address", "Contact", "Spouse", "Children", "Salary"])
            # Write each employee's data
            for emp in employees:
                writer.writerow(emp.to_list())
        print("All employee data saved successfully.\n")
    except Exception as e:
        print("Error while saving:", e)

# Function to read and show employee data from the CSV file
def show_employees():
    try:
        with open("employees.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            print("\nEmployee Details:")
            for row in reader:
                print("ID:", row[0], "| Name:", row[1], "| Address:", row[2], "| Contact:", row[3],
                      "| Spouse:", row[4], "| Children:", row[5], "| Salary:", row[6])
    except FileNotFoundError:
        print("No employee data found. Please add employees first.\n")
    except Exception as e:
        print("Error while reading:", e)

# Main part of the program
def main():
    employee_list = []

    while True:
        print("\nChoose an option:")
        print("1. Add Employee")
        print("2. Save & Show Employees")
        print("3. Exit")
        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            try:
                empid = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                address = input("Enter Address: ")
                contact = input("Enter Contact Number: ")
                spouse = input("Enter Spouse Name: ")
                children = input("Enter Number of Children: ")
                salary = input("Enter Salary: ")

                # Create Employee instance and add to list
                emp = Employee(empid, name, address, contact, spouse, children, salary)
                employee_list.append(emp)
                print("Employee added.\n")
            except Exception as e:
                print("Something went wrong:", e)

        elif choice == "2":
            # Save all employees to CSV and display them
            save_employees(employee_list)
            show_employees()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

main()

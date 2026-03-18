"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Week 7 Assignment 2
"""
# dictionary_retrieval.py

# This function creates and returns the employee dictionary
def create_employee_dictionary():
    # Define the dictionary with updated values
    employee = {
        "name": "Tatiana Tensai",
        "department": "Neurosurgery",
        "salary": 750000
    }
    
    # Return the dictionary so it can be used in other functions
    return employee


# This function retrieves specific values from the dictionary
def retrieve_employee_info(employee_data):
    # Access the department using its key
    department = employee_data["department"]
    
    # Access the salary using its key
    salary = employee_data["salary"]
    
    # Return both values
    return department, salary


# This function prints the retrieved values in the correct format
def print_employee_info(department, salary):
    # Print exactly as required in the assignment
    print(f"Department: {department} Salary: {salary}")


# Main function to control the program flow
def main():
    # Create the dictionary
    employee = create_employee_dictionary()
    
    # Retrieve values from the dictionary
    department, salary = retrieve_employee_info(employee)
    
    # Print the results
    print_employee_info(department, salary)


# Ensures the program runs when executed
if __name__ == "__main__":
    main()
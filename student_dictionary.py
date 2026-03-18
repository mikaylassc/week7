"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Week 7 Assignment 1
"""
# student_dictionary.py
# This function creates a dictionary with student information
def create_student_dictionary():
    # Define the dictionary with updated key-value pairs
    student = {
        "name": "Jade West",
        "age": 22,
        "major": "Criminal Justice",
    }
    
    return student


# This function prints the student dictionary
def print_student_dictionary(student_data):
    # Print the dictionary exactly as required
    print(student_data)


# Main function to control the program flow
def main():
    # Create the dictionary
    student = create_student_dictionary()
    
    # Print the dictionary
    print_student_dictionary(student)


# Ensures the program runs when executed directly
if __name__ == "__main__":
    main()
"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Week 7 Assignment 3
"""
# dictionary_update_remove.py

# This function creates and returns the original car dictionary
def create_car_dictionary():
    # Define the dictionary exactly as required
    car = {
        "brand": "Hyundai",
        "model": "Santa Fe",
        "year": 2016
    }
    
    return car


# This function updates and removes values in the dictionary
def update_and_modify_car(car_data):
    # Update the year to 2025
    car_data["year"] = 2025
    
    # Remove the "model" key from the dictionary
    del car_data["model"]
    
    # Return the updated dictionary
    return car_data


# This function prints the final dictionary
def print_car_dictionary(updated_car):
    # Print the dictionary exactly as required
    print(updated_car)


# Main function to control program flow
def main():
    # Create the original dictionary
    car = create_car_dictionary()
    
    # Update and modify the dictionary
    updated_car = update_and_modify_car(car)
    
    # Print the updated dictionary
    print_car_dictionary(updated_car)


# Ensures the program runs when executed
if __name__ == "__main__":
    main()
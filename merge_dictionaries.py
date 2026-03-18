"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Week 7 Assignment 4
"""
# merge_dictionaries.py

# This function creates and returns the first dictionary
def create_first_dictionary():
    dict1 = {
        "a": 2,
        "b": 4
    }
    
    return dict1


# This function creates and returns the second dictionary
def create_second_dictionary():
    dict2 = {
        "b": 6,
        "c": 8
    }
    
    return dict2


# This function merges the two dictionaries
def merge_dictionaries(dict1, dict2):
    # Create a copy of the first dictionary to avoid modifying the original
    merged_dict = dict1.copy()
    
    # Update the copy with values from the second dictionary
    # If a key exists in both, dict2's value will overwrite dict1's value
    merged_dict.update(dict2)
    
    return merged_dict


# This function prints the merged dictionary
def print_merged_dictionary(merged_dict):
    # Print the dictionary exactly as required
    print(merged_dict)


# Main function to control program flow
def main():
    # Create both dictionaries
    dict1 = create_first_dictionary()
    dict2 = create_second_dictionary()
    
    # Merge the dictionaries
    merged_dict = merge_dictionaries(dict1, dict2)
    
    # Print the result
    print_merged_dictionary(merged_dict)


# Ensures the program runs when executed
if __name__ == "__main__":
    main()
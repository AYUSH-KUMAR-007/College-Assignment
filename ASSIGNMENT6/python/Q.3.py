def check_parentheses_balance(s):
    """Check if the number of opening and closing parentheses are equal."""
    open_count = 0
    close_count = 0
    
    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            close_count += 1
            
    return open_count == close_count

# Example usage
if __name__ == "__main__":
    test_string = input("Enter a string: ")
    if check_parentheses_balance(test_string):
        print("The number of opening and closing parentheses are equal.")
    else:
        print("The number of opening and closing parentheses are not equal.")

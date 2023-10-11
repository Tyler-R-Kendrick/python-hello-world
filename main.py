# ignore missing module docstring
# pylint: disable=C0114

# write a function that takes a string and returns the string reversed
def reverse_string(string):
    """
    Reverses the order of characters in a given string.

    Args:
        string (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    return string[::-1]

# call the function with "hello world" as the argument and print the result
print(reverse_string("hello world"))

# utility.py
def input_number(msg, min_value=None, max_value=None):
    """Prompt user for an integer within optional range."""
    while True:
        inp = input(msg).strip()
        try:
            value = int(inp)
        except ValueError:
            print("Please enter a valid number!")
            continue

        if (min_value is not None and value < min_value) or \
           (max_value is not None and value > max_value):
            print(f"Value must be between {min_value} and {max_value}.")
            continue

        return value

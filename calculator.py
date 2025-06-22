def validate_numbers(nums):
    '''checks for any invalid characs in string'''
    invalid_chars = find_invalid_chars(nums)
    if invalid_chars:
        raise ValueError("Invalid number: "+', '.join(invalid_chars))
    negatives = find_negative_numbers(nums)
    if negatives:
        raise ValueError(
                f"negative numbers not allowed {', '.join(negatives)}")

def find_negative_numbers(nums):
    '''Finds negative numbers in the input list.'''
    return [num for num in nums if int(num) < 0]

def find_invalid_chars(nums):
    '''Checks if the input contains any invalid characters.'''
    invalid_chars =  [num for num in nums if not is_valid_number(num)]
    return invalid_chars

def is_valid_number(num):
    """Checks if the input is a valid number."""
    return num.isdigit() or (num.startswith('-') and num[1:].isdigit())

def parse_input(input_string):
    """Parses the input string, validates tokens, and converts to integers."""
    if not input_string:
        return ',', []

    if input_string.startswith('//'):
        delimiter_line, input_string = input_string[2:].split('\n', 1)
        delimiter = delimiter_line
    else:
        delimiter = ','

    input_string = input_string.replace('\n', delimiter)
    tokens = input_string.split(delimiter)

    validate_numbers(tokens)

    return delimiter, list(map(int, tokens))

def cleanupdecorator(func):
    """Decorator to parse and validate string input for a calculator function."""
    def wrapper(*args, **kwargs):
        self_or_input = args[0] if args else None
        input_string = args[1] if len(args) > 1 else ''

        delimiter, numbers = parse_input(input_string)

        if not numbers:
            return 0

        modified_args = (
            (self_or_input, [delimiter] + numbers) if hasattr(self_or_input, '__class__')
            else ([delimiter] + numbers,)
        )

        return func(*modified_args, **kwargs)

    return wrapper


class StringCalculator:
    """Main class for string calculator operations."""
    def __init__(self):
        pass

    @cleanupdecorator
    def add(self,numbers) -> int:
        """
        Adds numbers from a string input, handling custom delimiters and negative numbers.
        If the input is empty, returns 0.
        Raises ValueError for invalid numbers or negative numbers.
        """
        delimiter , *numbers = numbers
        if delimiter == "o":
            total_sum = 0
            for i in numbers:
                if i % 2 != 0:
                    total_sum+= i
            return total_sum
        return sum(numbers)
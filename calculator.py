def cleanupdecorator(func):
    """Decorator to handle string input parsing and validation for calculator."""
    def wrapper(self, *args, **kwargs):
        numbers = args[0] if args else ''
        if not numbers:
            return 0
        # Check for custom delimiter
        if numbers.startswith('//'):
            delimiter, numbers = numbers[2:].split('\n', 1)
        else:
            delimiter = ','

        # Split the input string by commas and newlines
        nums_list = numbers.replace('\n', ',').split(delimiter)

        # checking for invalid characters
        invalid_chars = [num for num in nums_list if not num.isdigit() and not (
            num.startswith('-') and num[1:].isdigit())]

        if invalid_chars:
            raise ValueError(f"Invalid number: {', '.join(invalid_chars)}")

        # checking for negative numbers
        negatives = [num for num in nums_list if int(num) < 0]
        if negatives:
            raise ValueError(
                f"negative numbers not allowed {', '.join(negatives)}")
        nums_list = [int(i) for i in nums_list]
        return func(self, nums_list)
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

        return sum(numbers)



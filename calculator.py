def add(numbers: str) -> int:
    if not numbers:
        return 0
    # Check for custom delimiter
    if numbers.startswith('//'):
        delimiter, numbers = numbers[2:].split('\n', 1)
    else:
        delimiter = ','
    # Split the input string by commas and newlines
    nums_list = numbers.replace('\n', ',').split(delimiter)
    total = 0
    for num in nums_list:
        try:
            total += int(num)
        except ValueError as e:
            raise ValueError(f"Invalid number: {num}") from e
    return total

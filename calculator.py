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

    total = 0
    for num in nums_list:
        total += int(num)
    return total

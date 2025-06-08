def add(numbers: str) -> int:
    if not numbers:
        return 0

    nums_list = numbers.split(',')
    total = 0
    for num in nums_list:
        try:
            total += int(num)
        except ValueError as e:
            raise ValueError(f"Invalid number: {num}") from e
    return total

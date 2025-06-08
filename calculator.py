def add(numbers: str) -> int:
    if not numbers:
        return 0

    nums_list = numbers.split(',')
    total = 0
    for num in nums_list:
        total += int(num)
    return total

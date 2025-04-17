import re

def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter = ",|\n"
    if numbers.startswith("//"):
        delimiter_line, numbers = numbers.split("\n", 1)
        delimiter = re.escape(delimiter_line[2:])

    num_list = re.split(delimiter, numbers)
    int_list = []
    negatives = []

    for num in num_list:
        if num:
            n = int(num)
            if n < 0:
                negatives.append(n)
            int_list.append(n)

    if negatives:
        raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

    return sum(int_list)

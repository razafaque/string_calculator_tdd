# String Calculator TDD  (Python)

TDD implementation of the classic String Calculator .

## Problem Statement

Create a calculator with a method `add(string numbers)` that returns the sum of comma-separated integers. Support new lines, custom delimiters, and throw exceptions for negative numbers.

## Features

- `add("")` → `0`
- `add("1")` → `1`
- `add("1,2")` → `3`
- Support unlimited numbers: `add("1,2,3")` → `6`
- Support newlines: `add("1\n2,3")` → `6`
- Custom delimiter: `add("//;\n1;2")` → `3`
- Negative numbers throw exception: `add("1,-2")` → ValueError

## Run Locally

### Setup

```bash
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
```

### Run Tests

```bash
pytest
```

## Commit Philosophy

Each step in development was guided by the TDD cycle:
- Red: Write a failing test
- Green: Write the minimum code to make it pass
- Refactor: Clean up without changing functionality

## License

MIT

# Lab1-MLOPS Calculator Project

This project is a Python calculator lab built with both `pytest` and `unittest` test suites.

It includes:
- Basic arithmetic functions (`fun1`, `fun2`, `fun3`, `fun4`)
- Financial functions (`profit_loss`, `simple_interest`, `compound_interest`)
- Automated tests in both testing frameworks

## Project Structure

```text
Lab1-MLOPS-/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   └── calculator.py
└── test/
		├── test_pytest.py
		└── test_unittest.py
```

## Installation & Setup

### 1) Clone the repository

```bash
git clone <your-repo-url>
cd Lab1-MLOPS-
```

### 2) Create and activate a virtual environment

#### macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows (PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

## Implemented Functions

Functions are located in `src/calculator.py`.

### Basic Math
- `fun1(x, y)`: returns `x + y`
- `fun2(x, y)`: returns `x - y`
- `fun3(x, y)`: returns `x * y`
- `fun4(x, y, z)`: returns `x + y + z`

### Financial
- `profit_loss(cost_price, selling_price)`
	- Returns net amount: `selling_price - cost_price`
	- Positive = profit, negative = loss

- `simple_interest(principal, rate, time)`
	- Formula: `(principal * rate * time) / 100`

- `compound_interest(principal, rate, time, compounds_per_year=1)`
	- Formula:
		`principal * (1 + rate / (100 * compounds_per_year)) ** (compounds_per_year * time) - principal`

## Running Tests

### Run pytest

```bash
pytest -q
```

### Run unittest

```bash
python -m unittest discover -s test -p "test_unittest.py" -q
```

## Current Test Coverage (by count)

- `pytest`: 14 tests
- `unittest`: 7 tests

## What Is Different From the Reference Lab1

Reference:
https://github.com/raminmohammadi/MLOps/tree/main/Labs/Github_Labs/Lab1

Compared to the reference Lab1, this project includes these key differences:

1. **Added financial calculator features**
	 - New functions: `profit_loss`, `simple_interest`, `compound_interest`
	 - Reference Lab1 focuses on the original four arithmetic functions.

2. **Expanded test suites**
	 - Added matching tests for all new financial functions in both:
		 - `test/test_pytest.py`
		 - `test/test_unittest.py`

3. **Improved pytest import reliability for this local layout**
	 - Added project-root path handling in `test/test_pytest.py` so imports work consistently in local execution.

4. **Updated project documentation**
	 - This README provides practical local setup/run instructions tailored to this repository.

## Notes

- Input validation is implemented for numeric checks in most functions.
- `compound_interest` validates that `compounds_per_year` is not zero.

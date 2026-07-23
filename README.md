# SMC Calculator / калькулятор

SMC-Calculator — simple interactive calculator originally written in Russian. This repository contains a small terminal calculator program with seven memory cells (SMC — Seven Memory Cells) and several utility modes (power, fraction to decimal, percent, random, square/cube roots, notes, and memory clear).

This README is present in both the repository default branch and the `ai` branch. The `ai` branch contains a refactored version of the calculator with safer expression evaluation and improved token handling.

## Description / Описание

- Program name: калькулятор.py
- Language: Python
- Purpose: interactive terminal calculator with memory cells and symbolic tokens (Russian tokens such as `пи`, `фи`, `тау`, `же`, `скорость света` and Latin `e`).

## Features / Возможности

- Seven memory cells (generic, fraction-to-decimal, power, random, percent, square root, cube root)
- Tokens/shortcuts for constants: `пи` (pi), `фи` (phi), `тау` (tau), `же` (g), `скорость света` (c), `e` (Euler's number)
- Modes: evaluate expression, power, fraction to decimal, random integer, square root, cube root, percentage, view/clear memory, notes
- `ai` branch: refactored code using safe AST-based evaluator (prevents arbitrary eval), improved token replacement using word boundaries, English comments, and better memory organization

## Requirements / Требования

- Python 3.8+

## Installation / Запуск

1. Clone the repository:

   git clone https://github.com/wertyopti/SMC-Calculator.git
   cd SMC-Calculator

2. To run the default branch version:

   python3 калькулятор.py

3. To run the refactored version from the `ai` branch:

   git fetch origin
   git checkout ai
   python3 калькулятор.py

Note: The filename contains Cyrillic characters (`калькулятор.py`). Ensure your shell and text editor support UTF-8 filenames. If your environment has issues with non-ASCII filenames, consider renaming the file to `smc_calculator.py`.

## Usage examples / Примеры

- Evaluate an expression (U):
  - Input: U → then `пи + 2` → Output: ~5.14159
- Power (S):
  - Input: S → число: 2 → степень: 8 → Output: 256
- Fraction to decimal (I):
  - Input: I → числитель: 1 → знаменатель: 2 → Output: 0.5
- Square root (QK):
  - Input: QK → 9 → Output: 3.0
- Cube root (CK):
  - Input: CK → -27 → Output: -3.0
- Percentage (%):
  - Input: % → число: 200 → процент: 10 → Output: 20.0
- Random (R):
  - Input: R → Output: random integer (0..10000)
- Memory (M) and clear (MAD) are available in the menu

## Notes

- The `ai` branch contains important safety and usability changes. If you plan to use the program in automated contexts or accept user-provided expressions, prefer the `ai` branch version since it replaces `eval` with a safe AST evaluator.

## Contributing / Вклад

- You can open issues or pull requests. Suggested improvements:
  - Rename the main script to use ASCII filename
  - Add unit tests for the evaluator and token replacements
  - Add localization / full English UI

## License

This project does not include a license file. Add a LICENSE if you intend to allow reuse.

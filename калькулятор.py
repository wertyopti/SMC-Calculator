import random
import time
import re
import ast
import operator

# SMC Calculator v1.3.6
# English comments are added. This file was refactored to:
# - improve token replacement using regex word boundaries
# - provide a safe arithmetic evaluator (no direct eval)
# - use a memory dictionary for all stored values
# - add comments and consistent formatting

# Loading animation
print("SMC Calculator v1.3.6")
print("Загрузка технологий...")
print()
modules = [
    "SevenMemoryCells (SMC)",
    "Memory All Delete (MAD)",
    "NotebookMemoryCell (NMC)",
    "Константы: π, e, τ, φ, c, g",
    "Графический интерфейс загрузки"
]

total = len(modules)
for i, module in enumerate(modules, 1):
    bar = "█" * i + "░" * (total - i)
    # Print a single-line progress bar for each module
    print(f"\r[{bar}] {i}/{total} {module}", end="")
    time.sleep(0.5)
print()
print("\n✅ Все технологии загружены!")
print()
print("""
╔═══════════════════════════════════════════════════╗
║     SMC Calculator                                 ║
║     SevenMemoryCells Technology (SMC)              ║
║     + MAD (Memory All Delete)                      ║
║     + NMC (NotebookMemoryCell)                     ║
║     + NMCD (NotebookMemoryCellDelete)              ║
╚═══════════════════════════════════════════════════╝
""")

# Memory storage (Seven memory cells and related values)
memory = {
    'd': 0.0,      # generic memory
    'di': 0.0,     # decimal memory (fraction -> decimal)
    'ds': 0.0,     # power memory
    'dqk': 0.0,    # square root memory
    'dck': 0.0,    # cube root memory
    'dp': 0.0,     # percent memory
    'dr': 0.0      # random memory
}

# Physical / mathematical constants
CONSTANTS = {
    'пи': 3.141592653589793,           # pi (Cyrillic token)
    'фи': 1.618033988749895,           # golden ratio (phi)
    'тау': 6.283185307179586,          # tau = 2*pi
    'же': 9.80665,                     # gravitational acceleration (token used in original)
    'скорость света': 299792458,       # speed of light
    'e': 2.718281828459045             # Euler's number (Latin 'e')
}

# Precompile regex for finding whole-word tokens (longer tokens first)
# We will build a list of tokens from CONSTANTS and memory keys with Russian words where needed.
# Use word boundaries so substrings are not accidentally replaced.

def build_replacement_pairs():
    pairs = {}
    # Add constant tokens
    for k, v in CONSTANTS.items():
        pairs[k] = str(v)
    # Add memory tokens (use Russian phrases matching original code)
    pairs['память степени'] = lambda: str(memory['ds'])
    pairs['память десятичная'] = lambda: str(memory['di'])
    pairs['память'] = lambda: str(memory['d'])
    pairs['память рандом'] = lambda: str(memory['dr'])
    pairs['память корня квадрата'] = lambda: str(memory['dqk'])
    pairs['память корня куба'] = lambda: str(memory['dck'])
    pairs['память процент'] = lambda: str(memory['dp'])
    return pairs

REPLACEMENT_PAIRS = build_replacement_pairs()
# Sort token keys by length descending so longer multi-word tokens match first
SORTED_TOKENS = sorted(REPLACEMENT_PAIRS.keys(), key=len, reverse=True)

# Safe arithmetic evaluator using ast: only allow simple arithmetic operations.
ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.FloorDiv: operator.floordiv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos
}


def safe_eval(expr: str):
    """Evaluate a numeric expression safely using AST.
    Allowed nodes: Expression, BinOp, UnaryOp, Constant (numbers), parentheses.
    No function calls or names are permitted after token replacement.
    """

    # Parse into AST
    try:
        tree = ast.parse(expr, mode='eval')
    except Exception as exc:
        raise ValueError(f'Invalid expression: {exc}')

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return float(node.value)
            else:
                raise ValueError('Only numeric constants are allowed')
        # Support older AST Num nodes
        if hasattr(ast, 'Num') and isinstance(node, ast.Num):
            return float(node.n)
        if isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in ALLOWED_OPERATORS:
                raise ValueError(f'Operator {op_type} not allowed')
            left = _eval(node.left)
            right = _eval(node.right)
            return ALLOWED_OPERATORS[op_type](left, right)
        if isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type not in ALLOWED_OPERATORS:
                raise ValueError(f'Unary operator {op_type} not allowed')
            operand = _eval(node.operand)
            return ALLOWED_OPERATORS[op_type](operand)
        # Parentheses are represented by nested nodes; no special handling required
        raise ValueError(f'Unsupported expression node: {type(node)}')

    result = _eval(tree)
    return result


def zam(text: str) -> float:
    """Replace known tokens (constants and memory) in the input text and evaluate safely.

    The function matches whole words (word boundaries) to avoid accidental partial replacements.
    """
    if not isinstance(text, str):
        raise ValueError('Input must be a string')

    expr = text.strip()
    # Normalize comma decimals (if user used comma as decimal separator)
    expr = expr.replace(',', '.')

    # Perform token replacements. Longer tokens are replaced first.
    for token in SORTED_TOKENS:
        repl = REPLACEMENT_PAIRS[token]
        if callable(repl):
            value = repl()
        else:
            value = repl
        # Use regex word boundary to replace whole token occurrences (case-sensitive)
        pattern = r"\b" + re.escape(token) + r"\b"
        expr = re.sub(pattern, value, expr)

    # After replacements, expr should contain only numbers and arithmetic operators
    # Validate characters allowed (digits, operators, parentheses, dot, spaces)
    if not re.fullmatch(r"[0-9+\-*/%.()\s]+", expr):
        # If there are unexpected characters, it's safer to reject
        raise ValueError('Expression contains invalid characters after token replacement')

    # Evaluate safely
    result = safe_eval(expr)
    return result


# Main interactive loop
MENU = (
    "режим:\n"
    " I - перевод дроби в десятичную\n"
    " S - возведение в степень\n"
    " R - рандом\n"
    " U - обычный (evaluate expression)\n"
    " QK - корень квадрата\n"
    " CK - корень куба\n"
    " % - проценты\n"
    " M - посмотреть память\n"
    " MAD - очистка всей памяти\n"
    " Z - заметки (set/show)\n"
    " ZD - очистить заметки\n"
    " E - выход\n"
)

notes = ''

while True:
    # Prompt the user (menu is in Russian). English comments above explain behavior.
    a = input(MENU + 'Выберите режим: ').strip()

    if a.upper() == 'S':
        # Power: number ** exponent
        bi = input('число: ')
        ps = input('степень: ')
        try:
            b = zam(bi)
            p = zam(ps)
            memory['ds'] = b ** p
            print(memory['ds'])
        except Exception as exc:
            print('Ошибка:', exc)

    elif a.upper() == 'I':
        # Fraction to decimal: numerator / denominator
        bi = input('числитель (you may use constants like пи, тау, фи, же, скорость света, e): ')
        ps = input('знаменатель: ')
        try:
            b = zam(bi)
            p = zam(ps)
            memory['di'] = b / p
            print(memory['di'])
        except Exception as exc:
            print('Ошибка:', exc)

    elif a.upper() == 'Z':
        # Notes: set or show
        if notes == '':
            notes = input('заметки: ')
        else:
            print('notes:', notes)

    elif a.upper() == 'ZD':
        notes = ''
        print('заметки очищены')

    elif a.upper() == 'R':
        # Random integer between 0 and 10000
        c = random.randint(0, 10000)
        print(c)
        memory['dr'] = c

    elif a == '%':
        # Percentage: (number * percent) / 100
        bi = input('число: ')
        ps = input('процент: ')
        try:
            b = zam(bi)
            p = zam(ps)
            memory['dp'] = b * p / 100.0
            print(memory['dp'])
        except Exception as exc:
            print('Ошибка:', exc)

    elif a.upper() == 'U':
        # Evaluate an expression and store in generic memory 'd'
        bi = input('пример (you may use constants like пи, тау, фи, же, скорость света, e): ')
        try:
            memory['d'] = zam(bi)
            print(memory['d'])
        except Exception as exc:
            print('Ошибка:', exc)

    elif a.upper() == 'QK':
        # Square root
        bi = input('введите число: ')
        try:
            b = zam(bi)
            if b >= 0:
                memory['dqk'] = b ** 0.5
                print(memory['dqk'])
            else:
                print('ошибка: отрицательное число')
        except Exception as exc:
            print('Ошибка:', exc)

    elif a.upper() == 'CK':
        # Cube root (works for negative numbers as well)
        bi = input('введите число: ')
        try:
            b = zam(bi)
            # cube root handling for negatives
            if b >= 0:
                memory['dck'] = b ** (1/3)
            else:
                memory['dck'] = -((-b) ** (1/3))
            print(memory['dck'])
        except Exception as exc:
            print('Ошибка:', exc)

    elif a.upper() == 'M':
        # Show all memory cells
        print('память:', memory['d'],
              'память рандом:', memory['dr'],
              'память степени:', memory['ds'],
              'память процент:', memory['dp'],
              'память корня квадрата:', memory['dqk'],
              'память корня куба:', memory['dck'],
              'память десятичная:', memory['di'])

    elif a.upper() == 'MAD':
        # Clear all memory cells
        for k in memory:
            memory[k] = 0.0
        print('память очищена')

    elif a == '67':
        # Easter: print '67' many times
        print('67' * 10000)

    elif a.upper() == 'E':
        # Exit the program
        break

    else:
        print('ошибка: неизвестный режим')

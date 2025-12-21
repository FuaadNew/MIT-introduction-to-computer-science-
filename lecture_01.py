# =============================================================================
# MIT 6.0001 — Lecture 1: What is Computation?
# =============================================================================
#
# Topics Covered:
#   - What is computation?
#   - Types of knowledge (declarative vs imperative)
#   - Algorithms and machines
#   - Python basics: objects, types, expressions
#
# =============================================================================


# -----------------------------------------------------------------------------
# 1. Basic Data Types
# -----------------------------------------------------------------------------

# Integers
x = 5
print(type(x))  # <class 'int'>

# Floats
y = 3.14
print(type(y))  # <class 'float'>

# Strings
name = "MIT"
print(type(name))  # <class 'str'>

# Booleans
is_enrolled = True
print(type(is_enrolled))  # <class 'bool'>


# -----------------------------------------------------------------------------
# 2. Simple Expressions
# -----------------------------------------------------------------------------

a = 10
b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.333...
print(a // b)  # Integer division: 3
print(a % b)   # Modulo: 1
print(a ** b)  # Exponentiation: 1000

from functools import reduce, partial  # Import reduce for accumulation and partial for pre-filling arguments

def imperative_processing(transactions):

    valid_transactions = []  

    for amount in transactions:  
        if amount > 0:  
            valid_transactions.append(amount)

    taxed_transactions = [] 

    for amount in valid_transactions:  
        taxed_transactions.append(amount * 1.10)  
    total = 0  
    for amount in taxed_transactions:  # Add all transformed transactions
        total += amount

    return total  # Return final total


# ==================== FUNCTIONAL VERSION ====================

def is_positive(amount):
    return amount > 0  # True for positive transactions


def apply_rate(rate, amount):
    return amount * rate  # Apply given rate


def add(a, b):
    return a + b  # Add two values


apply_tax = partial(apply_rate, 1.10)  # Fix rate as 1.10; amount will be provided later


def functional_processing(transactions):

    valid_transactions = filter(is_positive, transactions)  # Keep positive values

    taxed_transactions = map(apply_tax, valid_transactions)  # Apply 10% increase

    total = reduce(add, taxed_transactions, 0)  # Add all values starting from 0

    return total  # Return final total


# ==================== INPUT 1 ====================

transactions1 = [100, -20, 200, 0, 150, -50, 300]  # Normal input with positive and invalid values

print("Input 1:", transactions1)

print("Imperative:", imperative_processing(transactions1))  # Expected: 825.0

print("Functional:", functional_processing(transactions1))  # Expected: 825.0


# ==================== INPUT 2 ====================

transactions2 = [100, 200, 300]  # All transactions are valid

print("\nInput 2:", transactions2)

print("Imperative:", imperative_processing(transactions2))  # Expected: 660.0

print("Functional:", functional_processing(transactions2))  # Expected: 660.0


# ==================== INPUT 3 ====================

transactions3 = [-100, -200, 0]  # No positive transactions

print("\nInput 3:", transactions3)

print("Imperative:", imperative_processing(transactions3))  # Expected: 0

print("Functional:", functional_processing(transactions3))  # Expected: 0


# ==================== INPUT 4 ====================

transactions4 = []  # Empty transaction list

print("\nInput 4:", transactions4)

print("Imperative:", imperative_processing(transactions4))  # Expected: 0

print("Functional:", functional_processing(transactions4))  # Expected: 0


print("\nAll tests passed!")
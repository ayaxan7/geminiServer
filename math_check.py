import re
def is_mathematical_expression(text):
    """
    Checks if a string represents a valid mathematical expression.
    """
    # Clean and check empty input
    text = text.replace(" ", "").strip()
    if not text:
        return False

    # Allow only valid mathematical symbols, numbers, and functions
    if not re.match(r'^[0-9+\-*/%^().,eE]+$', text):
        return False

    # Ensure there's at least one math operator (e.g., `+`, `-`, `*`, `/`)
    operators = {'+', '-', '*', '/', '^', '%'}
    if not any(op in text for op in operators):
        return False

    return True

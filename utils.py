def format_result(value):
    """Format a numeric result for display."""
    if isinstance(value, float):
        if value == int(value):
            return str(int(value))
        return f"{value:.4f}"
    return str(value)


def validate_input(value):
    """Check if a value is a valid number."""
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False


def clamp(value, min_val, max_val):
    """Clamp a value between min and max."""
    return max(min_val, min(value, max_val))

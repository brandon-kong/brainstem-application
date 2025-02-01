def comma_separated_number(number: int) -> str:
    return "{:,}".format(number)

def format_seconds(seconds: float) -> str:
    """
    Format seconds depending on the number of hours, minutes, and seconds
    """
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if hours > 0:
        return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"
    elif minutes > 0:
        return f"{int(minutes)}m {int(seconds)}s"
    elif seconds >= 1:
        return f"{seconds:.2f}s"
    else:
        # get milliseconds
        milliseconds = seconds * 1000

        if milliseconds >= 1:
            return f"{milliseconds:.2f}ms"
        else:
            return f"{milliseconds:.2f}μs"
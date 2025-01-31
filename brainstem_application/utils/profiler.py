def time_function(func):
    """
    Time a function
    """
    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Took {round(end_time - start_time, 3)} seconds")
        return result

    return wrapper
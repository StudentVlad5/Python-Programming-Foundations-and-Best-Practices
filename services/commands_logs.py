from functools import wraps
from datetime import datetime

def log_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_msg = f"{timestamp} | Function: {func.__name__} | Args: {args} \n"
        with open("log_file.txt", "a", encoding="utf-8") as log_file:
            log_file.write(log_msg)
        
        return func(*args, **kwargs)
    return wrapper
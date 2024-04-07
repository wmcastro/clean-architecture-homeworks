def controller(funcion):
    def wrapper(*args, **kwargs):
        result = funcion(*args, **kwargs)
        return result
    return wrapper




def decorater_lower_case(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs).lower()
    return wrapper

@decorater_lower_case
def message(name):
     return f'{name}, recibiste un mensaje'

print(message("Lupita"))
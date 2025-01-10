# Manejo de errores en python
# un error simple

try:
    print(2/0)
except ZeroDivisionError as error_division:
    print("Error de division por cero")
    print(error_division)

print('###'*15)

print("El programa sigue funcionando")

# Manejo de errores de multiples: 

def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

print_exception_hierarchy(Exception)

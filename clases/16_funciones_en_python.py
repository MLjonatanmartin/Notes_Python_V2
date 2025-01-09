# declaración de una función

def greeting():
    return "Hello, World!"

# invocación de una función

hello = greeting()
print(hello)

# declaración de una función con parámetros

def greeting(name, lastname, profession):
    name.lower()
    lastname.lower()
    profession.lower()

    return f"Hello, {name.capitalize()} {lastname.capitalize()}, I'm a {profession.capitalize()}"

# invocación de una función con parámetros

juan = greeting("Juan", "Pérez", "developer")
print(juan)

ana = greeting("Ana", "Gómez", "designer")
print(ana)

pedro = greeting("Pedro", "Sánchez", "engineer")
print(pedro)
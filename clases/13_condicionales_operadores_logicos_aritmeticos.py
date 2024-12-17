# Uso de un condicional 

age = 18

if age >= 18:
    print('Bienvenido!')
else:
    print('No puedes entrar')

# Ejemplo de usuario

user = 'user90k'
password = '1234'

if (user == 'user90k') and (password == '1234'):
    print('Bienvenido al sistema')
else:
    print('Tu usuario o contraseña son incorrectos, por favor intelelo de nuevo')

# if anidado

budget = 4400
stockout = True

if stockout == True:
    if budget == 5000:
        print('Comprar productos al por mayor en cantidad')
    elif budget >= 4000:
        print('Comprar productos al por mayor')
    else:
        print('Estamos en quiebra')

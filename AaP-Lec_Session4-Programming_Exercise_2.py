def product(f, m):
    return (f / m)

m = float(input('Enter the mass in KG: '))
f = float(input('Enter force in Newtons: '))

print(f'The acceleration is {product(f, m)}')

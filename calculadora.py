# Calculadora simples
x = 1 
y=  2
z = x + y
print(z)

"""
#Entrada de dados
x = int(input("What's x? "))
y = int(input("What's y? "))
#Impressão e calculo
print(x + y)
# função int - converte em número inteiro

#Entrada de dados
x = float(input("What's x? "))
y = float(input("What's y? "))
#Impressão e calculo
print(round((x + y), 2))
# função float e round

#Entrada de dados
x = float(input("What's x? "))
y = float(input("What's y? "))
z = x / y
print(round(z,2))
print(f'{z:.2f}')

"""
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n**2

main()


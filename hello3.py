#Terceiro programa sobre Hello
name = input("What's your name? ")
#Remove os espaços em branco na string
name = name.strip()
#Coloca em maiusculo o nome
name = name.title()
#Divide o nome do usuário
first, last = name.split(" ")
#Imprimi Hello para o ususário
print(f"Hello, {first}")

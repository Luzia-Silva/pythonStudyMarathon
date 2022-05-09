nome = input("Informe o seu nome: ")
altura = float(input("Informe a sua altura: "))

# Como fazer o if e else no python
if altura > 1.65:
    print(nome + " é alto(a)!")
elif altura <= 156:
    # Exemplo de decisão encadeada, porque existe várias opções de decisão.
    print(nome + " é Mediano(a)!")
else:
    print(nome, " é baixo(a)!")

tabuada = int(input("Informe um valor para tabuada: "))

# Então se i for < 11 o laço executa
# no range (inicial, final(ou máximo valor), incremento(de quantas e quantas casinhas pular))
for i in range(1, 11, 1):
  # Quando você utiliza letras juntos com number é uma boa pratica transformá-los em str()
    print(str(tabuada) + "X" + str(i) + "=" + str(tabuada*i))

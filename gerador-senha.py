import random

print("****************")
print("GERADOR DE SENHA")
print("****************")

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
alfabeto_maiusculo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alfabeto_minusculo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
especiais = list("!@#$%&?")
lista = []

lista_str = (str(elemento) for elemento in lista)

numeros.extend(alfabeto_maiusculo)
numeros.extend(alfabeto_minusculo)
numeros.extend(especiais)

for n in range(0, 21):
    indice_aleatorio = random.randrange(len(numeros))
    senha = numeros[indice_aleatorio]
    lista.append(senha)

lista_sem_string = ''.join(lista_str)
print(f"Senha aleatória gerada: {lista_sem_string}")
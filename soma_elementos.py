#Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.
def soma_elementos(lista):
    soma = 0
    for x in lista:
        soma += x
    return soma
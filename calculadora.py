from xml.etree.ElementPath import ops


def soma(n1,n2):
    return n1+n2
def subtração(n1,n2):
    return n1-n2
def multiplicação(n1,n2):
    return n1*n2
def divisão(n1,n2):
    return n1/n2
ops = {
    "+": soma,
    "-": subtração,
    "*": multiplicação,
    "/": divisão,
} 
n1 = int (input("Digite o primeiro número: "))
operação = input ("Digite a operação: ")
n2 = int (input("Digite o segundo número: "))
operação_desejada = ops[operação]
print(operação_desejada(n1,n2))

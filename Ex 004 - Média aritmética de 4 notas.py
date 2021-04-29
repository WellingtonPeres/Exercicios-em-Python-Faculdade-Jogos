''' Desenvolva um programa em Python que receba 4 notas,
calcule e mostre a média aritmética entre elas.'''

print("Digite o primeiro valor: ")
nota1 = float(input())
print("Digite o segundo valor: ")
nota2 = float(input())
print("Digite o terceiro valor: ")
nota3 = float(input())
print("Digite o quarto valor: ")
nota4 = float(input())

mediaAritmetica = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média do aluno é {mediaAritmetica}")

#Exercise 01: Remove spaces from the name to count only the letters

name = input("Enter your name: ").replace(" ", "")
print(f"Your name has {len(name)} letters.")

#Exercício 02: Crie um programa onde o usuário digita dois valores e aparece a soma desses valores

valor_01 = int(input("Digite o primeiro valor: "))
valor_02 = int(input("Digite o segundo valor: "))

soma = valor_01 + valor_02
print(soma)
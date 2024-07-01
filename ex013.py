salario = float(input('Qual é o seu salário? '))
novo_salario = salario + (salario * 15 / 100)
print('Seu novo salário com 15% de aumento é R${:.2f}'.format(novo_salario))
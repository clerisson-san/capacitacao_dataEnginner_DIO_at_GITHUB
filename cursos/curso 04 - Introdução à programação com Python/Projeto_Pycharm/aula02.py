#Trabalhando com operadores e formatação

value1 = int(input("Entre com valor 01: "))
value2 = int(input("Entre om o valor 02: "))


soma = value1 + value2
subtract = value1 - value2
multiply = value1 * value2
divide = value1 / value2

print('\nSoma: {soma} - '
      '\nSubtração: {sub} - '
      '\nMultiplicação: {mult} - '
      '\nDivisao: {div}'
      .format(soma = soma,
              sub = subtract,
              mult = multiply,
              div = int(divide)))

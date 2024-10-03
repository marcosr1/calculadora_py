cont = input("deseja uma operação? digite sim ou não:")
while (cont == "sim"):
  #Aqui colhe os dados que a calculadora vai usar na operação logo abaixo
  num1 = input('bem vindo a sua calculadora, digite um numero:')
  num2 = input('digite o outro numero que deseja:')
  op = input("qual operação deseja fazer? soma= +, subtração= -, multiplicação= *, divisão= /")

  #Aqui os dados colhidos anteriormente são certificados e usados para fazer o calculo que o usuario deseja
  if op == "+":
    resultado = int(num1) + int(num2)
    print ("O resultado é: ",resultado)
  elif op == "-":
    resultado = int(num1) - int(num2)
    print ("O resultado é: ",resultado)
  elif op == "*":
    resultado = int(num1) * int(num2)
    print ("O resultado é: ",resultado)
  elif op == "/":
    resultado = int(num1) / int(num2)
    print ("O resultado é: ",resultado)
  else :
    print ("operação invalida")

  cont = input("deseja outra operação? digite sim ou não:")

else:
  print ("até a proxima")

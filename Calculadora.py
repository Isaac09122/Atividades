
 
print(" ██████  █████  ██       ██████ ██    ██ ██       █████  ██████   ██████  ██████   █████   ")
print("██      ██   ██ ██      ██      ██    ██ ██      ██   ██ ██   ██ ██    ██ ██   ██ ██   ██   ")
print("██      ███████ ██      ██      ██    ██ ██      ███████ ██   ██ ██    ██ ██████  ███████    ")
print("██      ██   ██ ██      ██      ██    ██ ██      ██   ██ ██   ██ ██    ██ ██   ██ ██   ██     ")
print(" ██████ ██   ██ ███████  ██████  ██████  ███████ ██   ██ ██████   ██████  ██   ██ ██   ██   ")
print("                                                                                           ")
print("                                                                                          ")

while True:
    try:
       
        num1 = float(input("Digite o primeiro número: "))
        
       
        num2 = float(input("Digite o segundo número: "))
        
        
        operacao = input("Digite a operação (+, -, *, /): ")

       
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                print("Erro: Não é possível dividir por zero.")
                continue
            resultado = num1 / num2
        else:
            print("Erro: Use apenas +, -, * ou /.")
            continue

        
        print("Resultado:", resultado)
        break

    except ValueError:
        print("Erro: Digite apenas números.")


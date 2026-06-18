# app.py - Calculadora de Índice de Massa Corporal (IMC)
# Este script é independente e NÃO está integrado com o index.html

# Função que calcula o IMC
def calcular_imc(peso, altura):
    """
    Calcula o IMC usando a fórmula: peso / (altura²)
    """
    # Verifica se a altura é zero para evitar erro de divisão
    if altura == 0:
        return "Erro: Altura não pode ser zero."
    
    # Realiza o cálculo
    imc = peso / (altura ** 2)
    # Arredonda o resultado para 2 casas decimais
    return round(imc, 2)


# Função que classifica o IMC de acordo com a OMS
def classificar_imc(imc):
    """
    Retorna a classificação do IMC e o nível de risco.
    """
    if imc < 18.5:
        return "Abaixo do peso (risco de desnutrição)"
    elif 18.5 <= imc < 25:
        return "Peso normal (saudável)"
    elif 25 <= imc < 30:
        return "Sobrepeso (risco aumentado)"
    elif 30 <= imc < 35:
        return "Obesidade grau I (risco alto)"
    elif 35 <= imc < 40:
        return "Obesidade grau II (risco muito alto)"
    else:
        return "Obesidade grau III (risco extremamente alto)"


# Função principal - executa o programa no terminal
def main():
    # Mensagem inicial
    print("=== Calculadora de IMC ===")
    print("Bem-vindo! Vamos calcular seu Índice de Massa Corporal.\n")
    
    while True:  # Loop para permitir vários cálculos
        try:
            # Solicita o peso
            peso = float(input("Digite seu peso em kg (ex: 70.5): "))
            
            # Validação: peso deve ser positivo
            if peso <= 0:
                print("❌ Erro: Peso deve ser maior que zero.\n")
                continue
                
            # Solicita a altura
            altura = float(input("Digite sua altura em metros (ex: 1.75): "))
            
            # Validação: altura deve ser positiva
            if altura <= 0:
                print("❌ Erro: Altura deve ser maior que zero.\n")
                continue
            
            # Calcula o IMC
            imc = calcular_imc(peso, altura)
            
            # Verifica se houve erro
            if isinstance(imc, str):
                print(imc)
                continue
            
            # Mostra resultados
            print(f"\n✅ Seu IMC é: {imc}")
            print(f"📊 Classificação: {classificar_imc(imc)}")
            
            # Pergunta se quer continuar
            continuar = input("\nDeseja calcular outro IMC? (s/n): ").strip().lower()
            if continuar != 's':
                print("👋 Obrigado por usar a calculadora de IMC!")
                break
                
        # Tratamento de erros de entrada
        except ValueError:
            print("❌ Erro: Por favor, digite apenas números.\n")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}\n")


# Executa o programa quando o arquivo é rodado diretamente
if __name__ == "__main__":
    main()# app.py - Calculadora de Índice de Massa Corporal (IMC)
# Este script é independente e NÃO está integrado com o index.html

# Função que calcula o IMC
def calcular_imc(peso, altura):
    """
    Calcula o IMC usando a fórmula: peso / (altura²)
    """
    # Verifica se a altura é zero para evitar erro de divisão
    if altura == 0:
        return "Erro: Altura não pode ser zero."
    
    # Realiza o cálculo
    imc = peso / (altura ** 2)
    # Arredonda o resultado para 2 casas decimais
    return round(imc, 2)


# Função que classifica o IMC de acordo com a OMS
def classificar_imc(imc):
    """
    Retorna a classificação do IMC e o nível de risco.
    """
    if imc < 18.5:
        return "Abaixo do peso (risco de desnutrição)"
    elif 18.5 <= imc < 25:
        return "Peso normal (saudável)"
    elif 25 <= imc < 30:
        return "Sobrepeso (risco aumentado)"
    elif 30 <= imc < 35:
        return "Obesidade grau I (risco alto)"
    elif 35 <= imc < 40:
        return "Obesidade grau II (risco muito alto)"
    else:
        return "Obesidade grau III (risco extremamente alto)"


# Função principal - executa o programa no terminal
def main():
    # Mensagem inicial
    print("=== Calculadora de IMC ===")
    print("Bem-vindo! Vamos calcular seu Índice de Massa Corporal.\n")
    
    while True:  # Loop para permitir vários cálculos
        try:
            # Solicita o peso
            peso = float(input("Digite seu peso em kg (ex: 70.5): "))
            
            # Validação: peso deve ser positivo
            if peso <= 0:
                print("❌ Erro: Peso deve ser maior que zero.\n")
                continue
                
            # Solicita a altura
            altura = float(input("Digite sua altura em metros (ex: 1.75): "))
            
            # Validação: altura deve ser positiva
            if altura <= 0:
                print("❌ Erro: Altura deve ser maior que zero.\n")
                continue
            
            # Calcula o IMC
            imc = calcular_imc(peso, altura)
            
            # Verifica se houve erro
            if isinstance(imc, str):
                print(imc)
                continue
            
            # Mostra resultados
            print(f"\n✅ Seu IMC é: {imc}")
            print(f"📊 Classificação: {classificar_imc(imc)}")
            
            # Pergunta se quer continuar
            continuar = input("\nDeseja calcular outro IMC? (s/n): ").strip().lower()
            if continuar != 's':
                print("👋 Obrigado por usar a calculadora de IMC!")
                break
                
        # Tratamento de erros de entrada
        except ValueError:
            print("❌ Erro: Por favor, digite apenas números.\n")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}\n")


# Executa o programa quando o arquivo é rodado diretamente
if __name__ == "__main__":
    main()# app.py - Calculadora de Índice de Massa Corporal (IMC)
# Este script é independente e NÃO está integrado com o index.html

# Função que calcula o IMC
def calcular_imc(peso, altura):
    """
    Calcula o IMC usando a fórmula: peso / (altura²)
    """
    # Verifica se a altura é zero para evitar erro de divisão
    if altura == 0:
        return "Erro: Altura não pode ser zero."
    
    # Realiza o cálculo
    imc = peso / (altura ** 2)
    # Arredonda o resultado para 2 casas decimais
    return round(imc, 2)


# Função que classifica o IMC de acordo com a OMS
def classificar_imc(imc):
    """
    Retorna a classificação do IMC e o nível de risco.
    """
    if imc < 18.5:
        return "Abaixo do peso (risco de desnutrição)"
    elif 18.5 <= imc < 25:
        return "Peso normal (saudável)"
    elif 25 <= imc < 30:
        return "Sobrepeso (risco aumentado)"
    elif 30 <= imc < 35:
        return "Obesidade grau I (risco alto)"
    elif 35 <= imc < 40:
        return "Obesidade grau II (risco muito alto)"
    else:
        return "Obesidade grau III (risco extremamente alto)"


# Função principal - executa o programa no terminal
def main():
    # Mensagem inicial
    print("=== Calculadora de IMC ===")
    print("Bem-vindo! Vamos calcular seu Índice de Massa Corporal.\n")
    
    while True:  # Loop para permitir vários cálculos
        try:
            # Solicita o peso
            peso = float(input("Digite seu peso em kg (ex: 70.5): "))
            
            # Validação: peso deve ser positivo
            if peso <= 0:
                print("❌ Erro: Peso deve ser maior que zero.\n")
                continue
                
            # Solicita a altura
            altura = float(input("Digite sua altura em metros (ex: 1.75): "))
            
            # Validação: altura deve ser positiva
            if altura <= 0:
                print("❌ Erro: Altura deve ser maior que zero.\n")
                continue
            
            # Calcula o IMC
            imc = calcular_imc(peso, altura)
            
            # Verifica se houve erro
            if isinstance(imc, str):
                print(imc)
                continue
            
            # Mostra resultados
            print(f"\n✅ Seu IMC é: {imc}")
            print(f"📊 Classificação: {classificar_imc(imc)}")
            
            # Pergunta se quer continuar
            continuar = input("\nDeseja calcular outro IMC? (s/n): ").strip().lower()
            if continuar != 's':
                print("👋 Obrigado por usar a calculadora de IMC!")
                break
                
        # Tratamento de erros de entrada
        except ValueError:
            print("❌ Erro: Por favor, digite apenas números.\n")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}\n")


# Executa o programa quando o arquivo é rodado diretamente
if __name__ == "__main__":
    main()
def calcular_juros_simples(principal, taxa, tempo):
    
    juros = principal * taxa * tempo
    montante_final = principal + juros
    return juros, montante_final

def interativo():
    try:
        principal = float(input("Digite o valor inicial (Principal): R$ "))
        taxa = float(input("Digite a taxa de juros anual (em %): ")) / 100
        tempo = float(input("Digite o tempo de investimento (em anos): "))
        
        juros, montante_final = calcular_juros_simples(principal, taxa, tempo)
        print(f"\nJuros acumulados: R$ {juros:.2f}")
        print(f"Montante final após {tempo} anos: R$ {montante_final:.2f}")
    except ValueError:
        print("Erro: Por favor, insira valores válidos.")

interativo()

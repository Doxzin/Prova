def calcular_area_comodos():# define o nome da função
    total_area = 0 # define a variavel da area total é igual a 0

    while True: # loop para pedir informação ate o usuario esteja satisfeito

        largura = float(input("Digite a largura do cômodo (em metros): ")) # pede a largura do comodo com o float ja que pode ser um numero quebrado
        #e o input espera o usuario digitar a informaçao
        comprimento = float(input("Digite o comprimento do cômodo (em metros): "))# mesma coisa que a de cima mas com o comprimento
        area_comodo = largura * comprimento # conta da area do comodo
        print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.") # printa a area do comodo  e mostra o resultado da conta

        total_area += area_comodo # coloca a area total como area do comodo

        mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower() #pergunta se quer ou não adicionar mais um comodo
        if mais_comodos != 's': # se a resposta da linha de cima for não interrompe o loop, senão ele continua
           break # o break sai do look caso seja não a resposta

    return total_area# retorna a valor da area total

area_total = calcular_area_comodos() # faz retornar o valor
print(f"A área total da casa é: {area_total:.2f} metros quadrados.")# printa a area do comodo  e mostra o resultado da conta
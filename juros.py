def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso): # define o nome da função e os parametros que vão chama-la

    juros_Diario = taxa_juros_anual / 365 / 100 # define o calculo para encontrar o juros diario

    juros = valor_principal * juros_Diario * dias_atraso # com o calculo de juros diarios conseguimos fazer a conta para encontrar o total de juros
    valor_total = valor_principal + juros # conta com o valor principal mais o juros para saber o valor total da conta
    return valor_total, juros # retorna o resultado do valor total e os juros

valor_principal = 1000.00 # valor principal pré definido
taxa_juros_anual = 5.0 # taxa de juros pré definida
dias_atraso = 30 # dias de atraso pré definido
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso) # faz retornar os dois valores
print(f"Valor total a ser pago: R${valor_total:.2f}")# as ultimas linhas apenas printam o que esta escrito nelas e os valores antes ditos: juros e valor total
print(f"Valor dos juros: R${juros:.2f}")
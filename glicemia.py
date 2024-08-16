def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial):  # define o nome da função e os parametros que vão chama-la

    if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200: # define que se a glicemia estiver maior que 126 em jejum ou 200 em prandial
        #retorna diabetes
        return "Diabetes"
    elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200: #define os valores que vao retornar ou não se a pessoa está pré-diabetica
        return "Pré-diabetes"
    else:
         return "Normal"# se não for nenhum dos valores em cima retorna que a glicemia esta tormal

glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): ")) #pede o valor da glicemia em jejum com float
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): "))#pede o valor da glicemia prandial com float

resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial) # faz retornar o resultado
print(f"O diagnóstico é: {resultado}")# printa o que esta escrico com "resultado"
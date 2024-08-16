def calcular_media_e_aprovacao(notas, nota_minima_aprovacao):# define o nome da função e os parametros que vão chama-la
    total_notas = 0 #define a variavel das notas
    num_alunos = len(notas)# obtem o numero de alunos
    aprovados = []# cria listas para manter o numero de aprovados e reprovados
    reprovados = []

    for aluno, nota in notas.items(): #pega o nome do aluno na lista 
    #e verifica se ele passou com base na nota minima de aprovaçao faz isso até a linha 14
        total_notas += nota
    if nota >= nota_minima_aprovacao:
         aprovados.append(aluno)
    else:
         reprovados.append(aluno)

    media_turma = total_notas / num_alunos # calcula a media da turma com base no numero de alunos

    return media_turma, aprovados, reprovados # retorna a media da turma e a quantidade de aprovados e reprovados

notas = { # lista que mantem o nome e a nota dos alinos
"Alice": 85,
"Bruno": 72,
"Carlos": 60,
"Diana": 95,
"Eduardo": 55
}

nota_minima_aprovacao = 70 # define a nota minima para aprovação

media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao) # faz retornar os dois valores

print(f"Média da turma: {media_turma:.2f}") # printa o que esta escrito e com os resultados
print(f"Alunos aprovados: {', '.join(aprovados)}")
print(f"Alunos reprovados: {', '.join(reprovados)}")
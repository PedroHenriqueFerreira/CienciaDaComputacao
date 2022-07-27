alunos = [
    {'nome': 'A', 'matricula': 1, 'curso': 'ADS',
        'notas': {'av1': 10, 'av2': 6, 'av3': 4}},
    {'nome': 'B', 'matricula': 2, 'curso': 'ADS',
        'notas': {'av1': 1, 'av2': 10, 'av3': 2}},
    {'nome': 'C', 'matricula': 3, 'curso': 'ADS',
        'notas': {'av1': 2, 'av2': 9, 'av3': 10}},
    {'nome': 'D', 'matricula': 4, 'curso': 'ADS',
        'notas': {'av1': 7, 'av2': 7, 'av3': 8}},
]


def cadastraAluno():
    print(f'--- Cadastrar Aluno ---')

    aluno = {
        'nome': input('Nome: '),
        'matricula': int(input('Matrícula: ')),
        'curso': input('Curso: '),
        'notas': {
            'av1': float(input('Nota av1: ')),
            'av2': float(input('Nota av2: ')),
            'av3': float(input('Nota av3: ')),
        }
    }

    alunos.append(aluno)


def listarAlunos():
    print('--- Lista de alunos ---')
    for aluno in alunos:
        print(f'{aluno["nome"]} - {aluno["matricula"]} - {aluno["curso"]}')


def listarMaioresNotas():
    print('--- Lista de maiores notas ---')
    av1 = alunos[0]['notas']['av1']
    aluno1 = alunos[0]
    av2 = alunos[0]['notas']['av2']
    aluno2 = alunos[0]
    av3 = alunos[0]['notas']['av3']
    aluno3 = alunos[0]
    
    for i in range(1, len(alunos)):
        if alunos[i]['notas']['av1'] > av1:
            av1 = alunos[i]['notas']['av1']
            aluno1 = alunos[i]
            
        if alunos[i]['notas']['av2'] > av2:
            av2 = alunos[i]['notas']['av2']
            aluno2 = alunos[i]
            
        if alunos[i]['notas']['av3'] > av3:
            av3 = alunos[i]['notas']['av3']
            aluno3 = alunos[i]

    print(f'Maior nota av1: {aluno1["nome"]} - {aluno1["notas"]["av1"]}')
    print(f'Maior nota av2: {aluno2["nome"]} - {aluno2["notas"]["av2"]}')
    print(f'Maior nota av3: {aluno3["nome"]} - {aluno3["notas"]["av3"]}')

def maiorMedia():
    print('--- Aluno com maior média ---')
    
    notas = alunos[0]['notas']
    
    media = (notas['av1'] + notas['av2'] + notas['av3']) / 3
    aluno = alunos[0]
    
    for i in range(1, len(alunos)):
        notas = alunos[i]['notas']
        mediaAtual = (notas['av1'] + notas['av2'] + notas['av3']) / 3
        
        if media < mediaAtual:
            media = mediaAtual
            aluno = alunos[i]

    print(f'Aluno com maior média: {aluno["nome"]} - {media:.2f}')

def listarSituacao():
    print('--- Situação dos alunos ---')    
    
    for i in alunos:
        media = (i['notas']['av1'] + i['notas']['av2'] + i['notas']['av3']) / 3

        if media >= 7:
            print(f'{i["nome"]} - {i["matricula"]} - {i["curso"]} - Aprovado')
        elif media >= 4:
            print(f'{i["nome"]} - {i["matricula"]} - {i["curso"]} - Avaliação final')
        else:
            print(f'{i["nome"]} - {i["matricula"]} - {i["curso"]} - Reprovado')
            
def situacaoDosAlunos():
    print('--- Situação dos alunos ---')
    
    aprovados = []
    avalicaoFinal = []
    reprovados = []
    
    for i in alunos:
        media = (i['notas']['av1'] + i['notas']['av2'] + i['notas']['av3']) / 3

        if media >= 7:
            aprovados.append(i)
        elif media >= 4:
            avalicaoFinal.append(i)
        else:
            reprovados.append(i)

    return { 'aprovados': aprovados, 'avalicaoFinal': avalicaoFinal, 'reprovados': reprovados }

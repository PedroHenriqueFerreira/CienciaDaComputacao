alunos = []

for i in range(5):
    print(f'--- Cadastrar {i + 1}° Aluno ---')
    
    aluno = { 
        'nome': input('Nome: '), 
        'matricula': int(input('Matrícula: ')), 
        'curso': input('Curso: ') 
    }
    
    alunos.append(aluno)
    

print('--- Lista de alunos ---')
for aluno in alunos:
    print(f'{aluno["nome"]} - {aluno["matricula"]} - {aluno["curso"]}')
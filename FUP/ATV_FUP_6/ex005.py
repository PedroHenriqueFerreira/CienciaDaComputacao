livros = []

def cadastrarLivro():
    print('----- Cadastro de Livro -----')
    titulo = input('Título: ').strip()
    autor = input('Autor: ').strip()
    ano = input('Ano: ').strip()
    
    livros.append({ 'titulo': titulo, 'autor': autor, 'ano': ano })
    
def listarLivros():
    print('----- Lista de Livros -----')
    
    for livro in livros:
        print(f"{livro['titulo']} - {livro['autor']} - {livro['ano']}")
        
def listarLivroPorNome():
    print('----- Listar livro por nome -----')
    nome = input('Nome: ').strip()
    
    for livro in livros:
        if livro['titulo'] == nome:
            print(f"{livro['titulo']} - {livro['autor']} - {livro['ano']}")
            return
        
    print('Nenhum livro encontrado')
        
def listarLivrosPorAutor():
    print('----- Listar livros por autor -----')
    autor = input('Autor: ').strip()
    
    encontrado = False
    for livro in livros:
        if livro['autor'] == autor:
            print(f"{livro['titulo']} - {livro['autor']} - {livro['ano']}")
            encontrado = True

    if not encontrado:
        print('Nenhum livro encontrado')

def removerLivro():
    print('----- Remover livro -----')
    nome = input('Nome: ').strip()
    
    for i in range(len(livros)):
        if livros[i]['titulo'] == nome:
            livros.pop(i)
            print('Livro removido com sucesso')
            return

    print('Nenhum livro encontrado')

def apagarTabelaLivros():
    print('----- Apagar Tabela de Livros -----')
    livros.clear()
    print('Tabela de livros apagada com sucesso')

def salvarLivros():
    print('----- Salvar Livros -----')
    arquivo = open('livros.txt', 'w')
    
    for livro in livros:
        arquivo.write(f"{livro['titulo']} - {livro['autor']} - {livro['ano']}\n")
        
    arquivo.close()

def carregarLivros():
    print('----- Carregar Livros -----')
    arquivo = open('livros.txt', 'r')
    
    livros.clear()    
    
    for linha in arquivo.readlines():
        linha = linha.split('-')
        
        livros.append({ 'titulo': linha[0].strip(), 'autor': linha[1].strip(), 'ano': linha[2].strip() })

    arquivo.close()

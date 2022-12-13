## Trabalho 5 de Laboratório
![Badge concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge)

## Descrição do repositório
Este repositório contém o trabalho 5 da disciplina de laborátorio de programação, que contém uma função para criar uma estrutura para uma heap. Além de funções para inserir e remover números inteiros nesta heap de forma que respeite os princípios dessa estrutura.

## Primeiros passos
Primeiramente é necessário ter o `gcc` e o `git` em sua máquina.

## Download
Cole o seguinte comando no terminal para obter o código do projeto.
```
$ git clone https://github.com/PedroHenriqueFerreira/Trabalho5Lab.git 
```

## Gerar bibliotecas
Cole o seguinte comando no terminal para gerar as bibliotecas do projeto.
```
$ gcc -c TR5_535770.c
```

## Compilação
Cole o seguinte comando no terminal para gerar o compilado do projeto.
```
$ gcc ./TR5_535770.o ./main.c -o main
``` 

## Execução
Cole um dos seguintes comandos para rodar o projeto:

Linux:
```
$ ./main
```

Windows:
```
$ ./main.exe
```

## Alterando a estrutura
- Primeiramente é necessário criar uma estrutura do tipo heap na função main do arquivo `main.c`. Para isso, basta chamar a função `HEAP_create` e passar como parâmetro: o tamanho da heap que será criada e uma função de comparação.
- Para adicionar elementos na heap basta chamar a função `HEAP_add` e passar como parâmetro: a estrutura da heap e um ponteiro void para o valor inteiro que será adicionado.
- Para remover elementos na heap basta chamar a função `HEAP_remove` e passar como parâmetro: a estrutura da heap.
- E para imprimir a heap, basta chamar a função `print` e passar como parâmetro: os elementos da heap e o tamanho da heap.

## Linguagens utilizadas
- `C`
## Trabalho 4 de Laboratório
![Badge concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge)

## Descrição do repositório
Este repositório contém o trabalho 4 da disciplina de laborátorio de programação, que contém uma função para criar uma estrutura para o vetor ordenado. Além de funções para inserir e remover números inteiros neste vetor de forma ordenada.

## Primeiros passos
Primeiramente é necessário ter o `gcc` e o `git` em sua máquina.

## Download
Cole o seguinte comando no terminal para obter o código do projeto.
```
$ git clone https://github.com/PedroHenriqueFerreira/Trabalho4Lab.git 
```

## Gerar bibliotecas
Cole o seguinte comando no terminal para gerar as bibliotecas do projeto.
```
$ gcc -c TR4_535770.c
```

## Compilação
Cole o seguinte comando no terminal para gerar o executável do projeto.
```
$ gcc ./TR4_535770.o ./main.c -o main
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
- Primeiramente é necessário criar uma estrutura do tipo vetor ordenado na função main do arquivo `main.c`. Para isso, basta chamar a função `VETORD_create` e passar como parâmetro: o tamanho do vetor que será criado e uma função de comparação.
- Para adicionar elementos no vetor basta chamar a função `VETORD_add` e passar como parâmetro: a estrutura do vetor e um ponteiro void para o valor inteiro que será adicionado.
- Para remover elementos no vetor basta chamar a função `VETORD_remove` e passar como parâmetro: a estrutura do vetor.
- E para imprimir o vetor, basta chamar a função `print` e passar como parâmetro: os elementos do vetor e o tamanho do vetor.

## Linguagens utilizadas
- `C`
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define TRUE 1
#define FALSE 0
#define STR_SIZE 64

typedef struct disciplina {
    int codigo;
    char nome[STR_SIZE];
    float nota_final;
} Disciplina;

typedef struct aluno {
    int matricula;
    char nome[STR_SIZE];
    char email[STR_SIZE];
    char endereco[STR_SIZE];
    char telefone[STR_SIZE];
    int qtd_disciplinas;
    Disciplina **disciplinas;
    struct aluno *esq, *dir;
} Aluno;

Aluno *raiz = NULL;

Aluno *buscar_aluno_recursivo(int matricula, Aluno *aux){
    if(aux == NULL){
        return NULL;    
    } else if(matricula == aux->matricula){
        return aux;
    } else if(matricula < aux->matricula){
        if (aux->esq != NULL){
            return buscar_aluno_recursivo(matricula, aux->esq);
        } else {
            return aux;
        }
    } else {
        if(aux->dir != NULL){
            return buscar_aluno_recursivo(matricula, aux->dir);
        }else{
            return aux;
        }
    }
}

int ler_matricula() {
    int matricula;
    printf("Digite a matrícula do aluno: ");
    scanf("%d", &matricula);

    return matricula;
}

Aluno *checa_buscar_aluno(int matricula) {
    Aluno *aluno_encontrado = buscar_aluno_recursivo(matricula, raiz);

    if (aluno_encontrado == NULL || aluno_encontrado->matricula != matricula) {
        printf("Aluno não encontrado!\n");
        return NULL;
    } 

    return aluno_encontrado;
}

void cadastrar_aluno() {
    printf("------- CADASTRAR ALUNO -------\n");
    int matricula = ler_matricula();

    Aluno *aluno_encontrado = buscar_aluno_recursivo(matricula, raiz);
    if (aluno_encontrado != NULL && aluno_encontrado->matricula == matricula) {
        printf("Aluno já cadastrado!\n");
        return;
    }

    Aluno *aluno = malloc(sizeof(Aluno));
    aluno->matricula = matricula;
    aluno->esq = NULL;
    aluno->dir = NULL;
    
    printf("Digite o nome do aluno: ");
    scanf("%s", aluno->nome);
    printf("Digite o email do aluno: ");
    scanf("%s", aluno->email);
    printf("Digite o endereço do aluno: ");
    scanf("%s", aluno->endereco);
    printf("Digite o telefone do aluno: ");
    scanf("%s", aluno->telefone);
    printf("Digite a quantidade de disciplinas do aluno: ");
    scanf("%d", &aluno->qtd_disciplinas);
    
    aluno->disciplinas = malloc(aluno->qtd_disciplinas * sizeof(Disciplina*));

    for (int i = 0; i < aluno->qtd_disciplinas; i++) {
        aluno->disciplinas[i] = malloc(sizeof(Disciplina));

        printf("Digite o nome da %d° disciplina: ", i + 1);
        scanf("%s", aluno->disciplinas[i]->nome);
        printf("Digite o código de %s: ", aluno->disciplinas[i]->nome);
        scanf("%d", &aluno->disciplinas[i]->codigo);
        printf("Digite a nota final de %s: ", aluno->disciplinas[i]->nome);
        scanf("%f", &aluno->disciplinas[i]->nota_final);
    }

    if (aluno_encontrado == NULL) {
        raiz = aluno;
    } else if (aluno->matricula < aluno_encontrado->matricula) { 
        aluno_encontrado->esq = aluno;
    } else {
        aluno_encontrado->dir = aluno;
    }

    printf("Aluno cadastrado com sucesso!\n");
}

void freeAll(Aluno *aux) {
    for (int i = 0; i < aux->qtd_disciplinas; i++) {
        free(aux->disciplinas[i]);
    }

    free(aux->disciplinas);
    free(aux);
}

Aluno *excluir_aluno_recursivo(Aluno *aux, int matricula) {
    if (aux == NULL) return NULL; 

    if (aux->matricula == matricula){
        if (aux->esq == NULL && aux->dir == NULL) {
            freeAll(aux);
            return NULL;
        } else if (aux->dir == NULL || aux->esq == NULL) {
            Aluno *aux2;
            if (aux->esq != NULL) {
                aux2 = aux->esq;
            } else {
                aux2 = aux->dir;
            }
        
            freeAll(aux);
            return aux2;
        } else {
            Aluno *aux2 = aux->esq;
            while(aux2->dir != NULL){
                aux2 = aux2->dir;
            }

            aux->matricula = aux2->matricula;
            strcpy(aux->nome, aux2->nome);
            strcpy(aux->email, aux2->email);
            strcpy(aux->endereco, aux2->endereco);
            strcpy(aux->telefone, aux2->telefone);
            aux->qtd_disciplinas = aux2->qtd_disciplinas;
            aux->disciplinas = aux2->disciplinas;

            aux2->matricula = matricula;
            aux2->disciplinas = NULL;
            aux2->qtd_disciplinas = 0;

            aux->esq = excluir_aluno_recursivo(aux->esq, matricula);  
 
            return aux;
        }
    } else {
        if (matricula < aux->matricula){
            aux->esq = excluir_aluno_recursivo(aux->esq, matricula);  
        } else {
            aux->dir = excluir_aluno_recursivo(aux->dir, matricula);
        }  

        return aux;
    }
}

void excluir_aluno() {
    printf("-------- EXCLUIR ALUNO --------\n");

    int matricula = ler_matricula();

    Aluno *aluno_encontrado = checa_buscar_aluno(matricula);
    if (aluno_encontrado == NULL) return;

    raiz = excluir_aluno_recursivo(raiz, matricula);

    printf("Aluno excluído com sucesso!\n");
}

void alterar_aluno() {
    printf("-------- ALTERAR ALUNO --------\n");

    int matricula = ler_matricula();

    Aluno *aluno_encontrado = checa_buscar_aluno(matricula);
    if (aluno_encontrado == NULL) return;
    
    char resposta;

    printf("Gostaria de alterar o nome do aluno? (s/n): ");
    scanf("%s", &resposta);
    if (resposta == 's') {
        printf("Digite o novo nome do aluno: ");
        scanf("%s", aluno_encontrado->nome);
    }

    printf("Gostaria de alterar o email do aluno? (s/n): ");
    scanf("%s", &resposta);
    if (resposta == 's') {
        printf("Digite o novo email do aluno: ");
        scanf("%s", aluno_encontrado->email);
    }

    printf("Gostaria de alterar o endereço do aluno? (s/n): ");
    scanf("%s", &resposta);
    if (resposta == 's') {
        printf("Digite o novo endereço do aluno: ");
        scanf("%s", aluno_encontrado->endereco);
    }

    printf("Gostaria de alterar o telefone do aluno? (s/n): ");
    scanf("%s", &resposta);
    if (resposta == 's') {
        printf("Digite o novo telefone do aluno: ");
        scanf("%s", aluno_encontrado->telefone);
    }

    printf("Aluno alterado com sucesso!\n");
}

void buscar_aluno() {
    printf("-------- BUSCAR ALUNO ---------\n");

    int matricula = ler_matricula();

    Aluno *aluno_encontrado = checa_buscar_aluno(matricula);
    if (aluno_encontrado == NULL) return;

    printf("Matrícula: %d\n", aluno_encontrado->matricula);
    printf("Nome: %s\n", aluno_encontrado->nome);
    printf("Email: %s\n", aluno_encontrado->email);
    printf("Endereço: %s\n", aluno_encontrado->endereco);
    printf("Telefone: %s\n", aluno_encontrado->telefone);

    float maior;
    int maiorPos;
    Disciplina *aux;

    printf("Disciplinas:\n");
    if (aluno_encontrado->qtd_disciplinas == 0) {
        printf("(VAZIO)\n");
    } 

    for (int i = 0; i < aluno_encontrado->qtd_disciplinas; i++) {
        maior = aluno_encontrado->disciplinas[i]->nota_final;
        maiorPos = i;

        for (int j = i; j < aluno_encontrado->qtd_disciplinas; j++) {
            if (maior < aluno_encontrado->disciplinas[j]->nota_final) {
                maior = aluno_encontrado->disciplinas[j]->nota_final;
                maiorPos = j;
            }
        }
        
        aux = aluno_encontrado->disciplinas[i];
        aluno_encontrado->disciplinas[i] = aluno_encontrado->disciplinas[maiorPos];
        aluno_encontrado->disciplinas[maiorPos] = aux;

        printf("Nome: %s | Código: %d | Nota Final: %.2f\n", 
            aluno_encontrado->disciplinas[i]->nome, 
            aluno_encontrado->disciplinas[i]->codigo, 
            aluno_encontrado->disciplinas[i]->nota_final
        );
    }
}

Aluno *buscar_alunos_recursivo(Aluno *aux) {
    if (aux == NULL) return NULL;

    if (aux->esq != NULL) buscar_alunos_recursivo(aux->esq);    

    printf("Matrícula: %d | Nome: %s | Email: %s | Endereço: %s | Telefone: %s\n", aux->matricula, aux->nome, aux->email, aux->endereco, aux->telefone);

    if (aux->dir != NULL) buscar_alunos_recursivo(aux->dir);
}

void buscar_alunos() {
    printf("----- BUSCAR TODOS ALUNOS -----\n");

    if (raiz == NULL) {
        printf("(VAZIO)\n");
        return;
    }

    buscar_alunos_recursivo(raiz);
}

void cadastra_disciplina(int matricula, int codigo, char nome[], float nota_final) {
    Aluno *aluno_encontrado = buscar_aluno_recursivo(matricula, raiz);
    aluno_encontrado->disciplinas[codigo] = malloc(sizeof(Disciplina));
    aluno_encontrado->disciplinas[codigo]->codigo = codigo;
    strcpy(aluno_encontrado->disciplinas[codigo]->nome, nome);
    aluno_encontrado->disciplinas[codigo]->nota_final = nota_final;
}

void cadastra_aluno(int matricula, char nome[], char email[], char endereco[], char telefone[], int qtd_disciplinas) {
    Aluno *aluno_encontrado = buscar_aluno_recursivo(matricula, raiz);

    Aluno *aluno = malloc(sizeof(Aluno));
    aluno->matricula = matricula;
    aluno->esq = NULL;
    aluno->dir = NULL;
    
    strcpy(aluno->nome, nome);
    strcpy(aluno->email, email);
    strcpy(aluno->endereco, endereco);
    strcpy(aluno->telefone, telefone);
    aluno->qtd_disciplinas = qtd_disciplinas;
    aluno->disciplinas = malloc(aluno->qtd_disciplinas * sizeof(Disciplina*));

    if (aluno_encontrado == NULL) {
        raiz = aluno;
    } else if (aluno->matricula < aluno_encontrado->matricula) { 
        aluno_encontrado->esq = aluno;
    } else {
        aluno_encontrado->dir = aluno;
    }
}

int main() {
    system("cls||clear");
    int opcao;

    cadastra_aluno(5, "Aluno 5", "aluno5@gmail.com", "Rua 5", "555555555", 1);
    cadastra_disciplina(5, 0, "Disciplina 5", 10.0);

    cadastra_aluno(2, "Aluno 2", "aluno2@gmail.com", "Rua 2", "222222222", 1);
    cadastra_disciplina(2, 0, "Disciplina 2", 10.0);

    cadastra_aluno(1, "Aluno 1", "aluno1@gmail.com", "Rua 1", "111111111", 1);
    cadastra_disciplina(1, 0, "Disciplina 1", 10.0);

    cadastra_aluno(4, "Aluno 4", "aluno4@gmail.com", "Rua 4", "444444444", 1);
    cadastra_disciplina(4, 0, "Disciplina 4", 10.0);

    cadastra_aluno(7, "Aluno 7", "aluno7@gmail.com", "Rua 7", "777777777", 1);
    cadastra_disciplina(7, 0, "Disciplina 7", 10.0);

    cadastra_aluno(3, "Aluno 3", "aluno3@gmail.com", "Rua 3", "333333333", 1);
    cadastra_disciplina(3, 0, "Disciplina 3", 10.0);

    cadastra_aluno(8, "Aluno 8", "aluno8@gmail.com", "Rua 8", "888888888", 1);
    cadastra_disciplina(8, 0, "Disciplina 8", 10.0);

    cadastra_aluno(9, "Aluno 9", "aluno9@gmail.com", "Rua 9", "999999999", 1);
    cadastra_disciplina(9, 0, "Disciplina 9", 10.0);

    cadastra_aluno(6, "Aluno 6", "aluno6@gmail.com", "Rua 6", "666666666", 1);
    cadastra_disciplina(6, 0, "Disciplina 6", 10.0);

    do {
        printf("---------- BEM VINDO ----------\n");
        printf("[0] - Sair da aplicação\n");
        printf("[1] - Cadastrar aluno\n");
        printf("[2] - Excluir aluno\n");
        printf("[3] - Alterar dados de um aluno\n");
        printf("[4] - Buscar dados de um aluno\n");
        printf("[5] - Buscar dados de todos os alunos\n");
        printf("-------------------------------\n");
        printf("Selecione uma opção: ");

        scanf("%d", &opcao);
        system("cls||clear");

        switch (opcao)
        {
            case 0:
                break;
            case 1:
                cadastrar_aluno();
                break;
            case 2:
                excluir_aluno();
                break;
            case 3:
                alterar_aluno();
                break;
            case 4:
                buscar_aluno();
                break;
            case 5:
                buscar_alunos();
                break;
            default:
                printf("Opção inválida\n");
                break;
        }
    } while (opcao != 0);

    printf("Saindo da aplicação...\n");

    return 0;
}
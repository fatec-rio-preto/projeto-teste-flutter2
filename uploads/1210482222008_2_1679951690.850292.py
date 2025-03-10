# -*- coding: utf-8 -*-
"""Cópia de LP2023 - Avaliação 01 - Exercício 02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fxK-0CR--V8e-YpRn41n8Jf5LfS7MlIW

Curso de Tecnologia em Análise e Desenvolvimento de Sistemas da Faculdade de Tecnologia de São José do Rio Preto
# Avaliação de Linguagem de Programação
## Prof. Dr. Henrique Dezani

---
### SUBMISSÃO

Para submeter a sua solução, siga as etapas:
1. Faça o download do código python clicando em File -> Download -> Download.py
2. Acesse o _link_
3. Faça o login usando seu número de matrícula
4. Faça o _upload_ do Exercício (arquivo que fez o _download_ do Colab na etapa 2). 

Não se esqueça de escolher o exerício correto durante a submissão.

---
### ENUNCIADO DO EXERCÍCIO 2

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.

Examplo

Dado o valor de entrada igual a `326`, a saída esperada é:

```
3 centenas, 2 dezenas e 6 unidades
```
Formato da entrada

A entrada consiste de um número inteiro positivo `numero` menor que 1000, informado pelo usuário.

Formato da saída

Descrição, por extenso, do número.

Entrada

```
12
```

Saída

```
1 dezena e duas unidades
```
"""

# Desenvolva seu programa aqui:
lista = ['unidade', 'dezena', 'centena']
n = int(input())

string_input = str(n)

if len(string_input) == 1:
    if int(string_input) > 1:
        print(f'{int(string_input)} unidades')
    else:
        print(f'{int(string_input)} unidade')
elif len(string_input) == 2:
    if int(string_input[0]) > 1:
        print(f'{int(string_input[0])} dezenas e ', end='')
        if int(string_input[1]) > 1:
            print(f'{int(string_input[1])} unidades')
        else:
            print(f'{int(string_input[1])} unidade')
    else:
        print(f'{int(string_input[0])} dezena e ', end='')
        if int(string_input[1]) > 1:
            print(f'{int(string_input[1])} unidades')
        else:
            print(f'{int(string_input[1])} unidade')
elif len(string_input) == 3:
    if int(string_input[0]) > 1:
        print(f'{int(string_input[0])} centenas, ', end='')
        if int(string_input[1]) > 1:
            print(f'{int(string_input[1])} dezenas e ', end='')
            if int(string_input[1]) > 1:
                print(f'{int(string_input[2])} unidades')
            else:
                print(f'{int(string_input[2])} unidade')
        else:
            print(f'{int(string_input[1])} dezena e ', end='')
            if int(string_input[2]) > 1:
                print(f'{int(string_input[2])} unidades')
            else:
                print(f'{int(string_input[2])} unidade')
    else:
        print(f'{int(string_input[0])} centena, ', end='')
        if int(string_input[1]) > 1:
            print(f'{int(string_input[1])} dezenas e ', end='')
            if int(string_input[2]) > 1:
                print(f'{int(string_input[2])} unidades')
            else:
                print(f'{int(string_input[2])} unidade')
        else:
            print(f'{int(string_input[1])} dezena e ', end='')
            if int(string_input[2]) > 1:
                print(f'{int(string_input[2])} unidades')
            else:
                print(f'{int(string_input[2])} unidade')


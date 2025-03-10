# -*- coding: utf-8 -*-
"""Cópia de LP2023 - Avaliação 01 - Exercício 02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oGxEKp8jHnwpDPhwFEPnRtO6sT1g4MJv

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

numero = int(input(''))
centena = int(numero /100)
numero = int(numero - (100* centena))
dezena = int(numero /10)
numero = int(numero -(10* dezena))
result = ''
if centena > 1:
  result = str(centena) + ' centenas'
elif centena == 1:
  result = str(centena) + ' centena'
if result != '' and dezena != 0:
  result = result + ' e '
if dezena > 1:
  result = result + str(dezena) + ' dezenas'
elif dezena == 1:
  result = result + str(dezena) + ' dezena'
if result != '' and numero != 0:
  result = result + ' e '
if numero > 1:
  result = result + str(numero) + ' unidades'
elif numero == 1:
  result = result + str(numero) + ' unidade'

if numero == 0 and result == '':
  result = '0 unidade'
print(result)
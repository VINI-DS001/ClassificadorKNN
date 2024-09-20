# Classificador KNN para Detecção de Imagens

Este repositório contém os códigos e documentação do projeto final da Unidade 01, no qual treinamos um classificador K-Nearest Neighbors (K-NN) para classificação de imagens com base em suas características. A tarefa envolve a extração de características das imagens, oriundas de datasets, e a implementação do classificador K-NN.

## Índice
- [Descrição do Projeto](#descrição-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação e Execução](#instalação-e-execução)
- [Treinamento e Escolha dos Algoritmos](#treinamento-e-escolha-dos-algoritmos)
    - [Extração de Características](#extração-de-características)
    - [Implementação do K-NN](#implementação-do-k-nn)
    - [Testes e Resultados](#testes-e-resultados)
- [Conjunto de Dados](#conjunto-de-dados)
- [Vídeos](#vídeos)

## Descrição do Projeto

Este projeto tem como objetivo construir um classificador de imagens utilizando o algoritmo KNN (K-Nearest Neighbors) para identificar imagens a partir de suas características extraídas. O processo inclui a extração de características visuais a partir de datasets, o treinamento do modelo K-NN e a realização de testes em novas imagens para verificar a precisão do classificador.

## Tecnologias Utilizadas
- Python 3.x
- Bibliotecas: `numpy`, `scikit-learn`, `opencv-python`
- Git/GitHub para controle de versão e colaboração

## Instalação e Execução

Para rodar o projeto localmente:

1. Clone o repositório:
    ```bash
    git clone https://github.com/VINI-DS001/ClassificadorKNN.git
    ```

2. Instale as dependências:
    ```bash
    pip install numpy
    ```

    ```bash
    pip install opencv-python
    ```

    ```bash
    pip install scikit-learn
    ```

3. Execute o arquivo de extração de caracteristicas e em seguida execute o script de treinamento do KNN:
    ```bash
    python caracteristicas.py
    ```

    ```bash
    python knn.py
    ```

## Treinamento e Escolha dos Algoritmos

### Extração de Características

Para a extração de características das imagens, utilizamos 3 datasets distintos, cada um com 2 mil imagens de calçados, sapatos, botas e sandalias, com dimensões 136 X 102. Através destes datasets foi possível extrair características para treinar o classificador KNN.

### Implementação do K-NN

Após extrair as características das imagens, treinamos o algoritmo **K-NN**. O K-NN é um classificador simples e eficiente, que funciona encontrando os "K" vizinhos mais próximos de uma amostra e utilizando a classe predominante entre eles como a predição final.

### Testes e Resultados

Testamos o modelo com diferentes valores de K (3, 5, 7) e o melhor desempenho foi obtido com **K=5**. A acurácia final do classificador no conjunto de testes foi de **90%**, o que mostra um bom desempenho para o problema de classificação de imagens utilizando o K-NN.

## Conjunto de Dados

O conjunto de dados utilizado para a extração de características para o treinamento do K-NN contém 6 mil imagens de três categorias, botas, sapatos e sandalias. Para a realização dos testes foram escolhidas imagens aleatórias que se encaixassem nessa categoria, para verificar a precisão do K-NN.

 - [Dataset: Shoe vs Sandal vs Boot](https://www.kaggle.com/datasets/hasibalmuzdadid/shoe-vs-sandal-vs-boot-dataset-15k-images)
 - [Imagens de Teste](https://unsplash.com/)

## Vídeos

 - [Imagens do dataset e Extração de características](https://drive.google.com/file/d/1NCOlwZpe5znfT9WJas4aFTB9go7RO8w1/view?usp=sharing)
 - [Execução do KNN](https://drive.google.com/file/d/1Y7jWFqEBX8ZKeKQPaVkPLwYS9v84BhsQ/view?usp=sharing)
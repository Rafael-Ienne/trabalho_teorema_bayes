# Estimador de exposição ocupacional à IA generativa

Este projeto consiste em uma aplicação web que utiliza o Teorema de Bayes para estimar a probabilidade de uma ocupação estar potencialmente exposta à Inteligência Artificial (IA) generativa. A aplicação é construída com base em dados de um estudo da Organização Internacional do Trabalho (OIT) e do Instituto Nacional de Pesquisa da Polônia (NASK), focando na influência de fatores geográficos, como a localização em países de alta renda, sobre essa exposição.

## 📄 Descrição do projeto

O objetivo principal deste trabalho é demonstrar a aplicação prática do Teorema de Bayes em um cenário real, utilizando o contexto da exposição de empregos à IA generativa. A aplicação é uma ferramenta educacional e demonstrativa que ilustra como inferências probabilísticas podem ser feitas a partir de dados observados.

Os dados iniciais para os cálculos são extraídos do estudo "IA generativa e Empregos: Um Índice Global Refinado de Exposição Ocupacional", que aponta que "25% do emprego global estão em ocupações potencialmente expostas à IA generativa, com participações maiores em países de renda alta (34%)". Para fins de demonstração do Teorema de Bayes, algumas probabilidades (como `P(B | ~A)`) foram inferidas/inventadas para completar o modelo.

## ✨ Funcionalidades

* **Cálculo da probabilidade condicional:** estima a probabilidade de uma ocupação estar exposta à IA generativa, dada a condição de estar ou não em um país de renda alta;
* **Transparência:** apresenta os valores de probabilidade (a priori, condicionais e marginais) que fundamentam o cálculo final, permitindo que o usuário entenda o raciocínio por trás do resultado;
* **Integração de dados do estudo:** incorpora diretamente os dados quantitativos fornecidos pelo estudo da OIT/NASK;
* **Estrutura completa:** demonstra a criação de um sistema web completo com um backend em Flask (Python) para a lógica e um frontend (HTML, CSS, JavaScript) para a interface do usuário.

## 🚀 Tecnologias utilizadas

* **Backend:**
    * [Python](https://www.python.org/)
    * [Flask](https://flask.palletsprojects.com/) (Microframework Web)
* **Frontend:**
    * [HTML5](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
    * [CSS3](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
    * [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)

## 📦 Configuração e instalação

Siga os passos abaixo para configurar e executar a aplicação em seu ambiente local.

### Pré-requisitos

Certifique-se de ter o Python 3 e o `pip` (gerenciador de pacotes do Python) instalados em sua máquina.

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Rafael-Ienne/trabalho_teorema_bayes.git
    ```

2.  **Instale as dependências do Python:**
    ```bash
    pip install Flask
    ```

4.  **Estrutura do projeto:**
    Certifique-se de que a estrutura de arquivos do seu projeto seja semelhante a esta:
    ```
    seu-repositorio/
    ├── app.py
    └── static/
        ├── css/
        │   └── style.css
        └── js/
            └── script.js
    └── templates/
        └── index.html
    ```

5.  **Execute a aplicação Flask:**
    ```bash
    python app.py
    ```
    O servidor Flask iniciará e você verá uma mensagem similar a:
    ```
    * Running on http://127.0.0.1:5000
      Press CTRL+C to quit
    ```

## 🌐 Como usar

1.  Após iniciar o servidor Flask (conforme a seção de instalação), abra seu navegador web e acesse o endereço fornecido: `http://127.0.0.1:5000/`;
2.  Você verá a página principal com a introdução do estudo da OIT/NASK;
3.  Na seção "Avaliador de exposição à IA generativa", marque (ou desmarque) a caixa de seleção "A ocupação está em um país de renda alta?";
4.  Clique no botão "Calcular exposição";
5.  O resultado será exibido na seção "Resultado", mostrando a probabilidade calculada e os detalhes das probabilidades que fundamentam o Teorema de Bayes.

## ⚙️ Probabilidades e fontes de dados

As probabilidades utilizadas no cálculo são as seguintes:

* **`P_A = 0.25`**: probabilidade a priori de uma ocupação estar potencialmente exposta à IA generativa. Baseada no estudo da OIT/NASK ("25% do emprego global estão em ocupações potencialmente expostas à IA generativa");
* **`P_NAO_A = 1 - P_A`**: probabilidade a priori de uma ocupação NÃO estar potencialmente exposta à IA generativa;
* **`P_B_DADO_A = 0.34`**: verossimilhança de uma ocupação estar em um país de alta renda, dado que ela está exposta à IA. Baseada no estudo da OIT/NASK ("participações maiores em países de renda alta (34%)" em relação às ocupações expostas);
* **`P_B_DADO_NAO_A = 0.20`**: verossimilhança de uma ocupação estar em um país de alta renda, dado que ela NÃO está exposta à IA. **Importante:** este valor foi *inventado* para fins de demonstração do Teorema de Bayes, pois não foi fornecido no trecho da notícia;
* **`P_B = (P_B_DADO_A * P_A) + (P_B_DADO_NAO_A * P_NAO_A)`**: probabilidade marginal de uma ocupação estar em um país de renda alta, calculada pela Lei da Probabilidade Total.

O código realiza o cálculo da probabilidade a posteriori `P(A|B)` ou `P(A|~B)` com base na seleção do usuário, aplicando a fórmula do Teorema de Bayes.

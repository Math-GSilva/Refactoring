# 🐜 Algoritmo ACO para o Problema da Mochila Binária

Este repositório contém a implementação do algoritmo de Otimização por Colônia de Formigas (ACO) para resolver o problema da mochila binária.

## 📌 Refatorações Realizadas

| Área | Descrição | Técnica Usada |
|------|-----------|----------------|
| Estrutura do código | Criação da classe `ACO` | Encapsulamento |
| Parâmetros | Parâmetros globais extraídos da lógica principal | Separação de responsabilidades |
| Modularização | Separação entre execução, lógica e testes | Modularização |
| Testes | Inclusão de `unittest` | Garantia de comportamento |
| Leitura | Comentários explicativos | Clareza e manutenção |

## 🔍 Testes

Os testes cobrem os seguintes casos:

- Avaliação válida de uma solução.
- Avaliação de solução que excede a capacidade.
- Validação de construção de solução factível.


## 🧪 Exemplo de execução

```text
Melhor Caminho (Itens Selecionados): [0, 1, 0, 0]
Valor Total Máximo Encontrado: 7
.
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

## 📚 Tecnologias

- Python 3.8+
- `unittest` para testes
- ACO customizado (algoritmo metaheurístico)

## 📁 Estrutura do Código

- `ACO` (classe principal com `avaliar`, `construir_solucao`, `executar`)
- Parâmetros ajustáveis via constantes
- Testes incluídos no mesmo arquivo para facilitar execução em notebooks e Google Colab

## 👨‍💻 Autores

Matheus Gabriel da Silva, Larissa Hoffmann, Lukas Thiago Rodrigues e Mateus Akira.

[Google Colab](https://colab.research.google.com/drive/1YycuUVIe_HPWZxiZpjDruT_yh4O0bj_r#scrollTo=D8CUaSx0V2bU)

[Repositório Original](https://github.com/EuMesmoMatheus/Formiguinha)

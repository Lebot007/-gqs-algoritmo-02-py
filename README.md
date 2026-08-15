# 🧮 Calculadora Básica em Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

Um programa simples em Python que realiza operações matemáticas básicas (soma, subtração, multiplicação e divisão) a partir de números digitados pelo usuário no terminal.

---

## 📖 O que o código faz

O programa pede ao usuário **dois números** e uma **operação** (`+`, `-`, `*` ou `/`), calcula o resultado e exibe no console. Ele foi pensado para ser simples de usar e de entender, servindo como exemplo de:

- Entrada de dados via `input()`;
- Conversão de tipos (`str` para `float`);
- Estrutura condicional `if / elif / else` para decidir qual operação executar;
- Tratamento de um caso de erro comum (divisão por zero).

---

## 📦 Pré-requisitos

- **Python 3** instalado ([download oficial](https://www.python.org/downloads/))
- Nenhuma biblioteca externa é necessária — o programa usa apenas recursos nativos do Python.

---

## 🚀 Como executar

1. Clone o repositório:

```bash
git clone https://github.com/Lebot007/-gqs-algoritmo-02-py.git
```

2. Entre na pasta do projeto:

```bash
cd gqs-algoritmo-02-py
```

3. Execute o script:

```bash
python main.py
```

> 💡 Em sistemas Linux/macOS, pode ser necessário usar `python3 main.py`.

---

## 🧪 Exemplo de saída

Ao rodar o programa, ele pede os valores interativamente. Seguem exemplos reais de execução:

**Exemplo 1 — Soma**
```text
=== Calculadora Básica ===
Digite o primeiro número: 10
Digite a operação desejada (+, -, *, /): +
Digite o segundo número: 5
Resultado: 15.0
```

**Exemplo 2 — Divisão**
```text
=== Calculadora Básica ===
Digite o primeiro número: 20
Digite a operação desejada (+, -, *, /): /
Digite o segundo número: 4
Resultado: 5.0
```

**Exemplo 3 — Divisão por zero (tratamento de erro)**
```text
=== Calculadora Básica ===
Digite o primeiro número: 10
Digite a operação desejada (+, -, *, /): /
Digite o segundo número: 0
Resultado: Erro: divisão por zero não é permitida
```

---

## 🧠 Detalhamento do código

### Função `calcular(num1, num2, operacao)`

Recebe os dois números e o símbolo da operação, e retorna o resultado (ou uma mensagem de erro).

```python
if operacao == '+':
    return num1 + num2
elif operacao == '-':
    return num1 - num2
elif operacao == '*':
    return num1 * num2
elif operacao == '/':
    if num2 == 0:
        return "Erro: divisão por zero não é permitida"
    return num1 / num2
else:
    return "Erro: operação inválida"
```

A estrutura `if / elif / else` compara o texto digitado (`operacao`) com cada símbolo possível e executa o cálculo correspondente. Dentro da divisão, há uma verificação extra (`if num2 == 0`) para evitar o erro de divisão por zero, que travaria o programa se não fosse tratado.

### Bloco principal (`if __name__ == "__main__":`)

```python
num1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))
```

- `input()` captura o que o usuário digita no terminal, sempre como texto (`str`);
- `float(...)` converte esse texto em número decimal, permitindo cálculos com casas decimais;
- Após coletar os dados, a função `calcular()` é chamada e o resultado é exibido com `print()`.

---

## 🗂️ Estrutura do código

| Parte do código | Responsabilidade |
|-----------------|------------------|
| `def calcular(num1, num2, operacao):` | Função que centraliza a lógica das quatro operações matemáticas |
| `input()` | Captura os valores e a operação digitados pelo usuário |
| `float()` | Converte o texto digitado em número decimal |
| `if / elif / else` | Decide qual operação matemática executar com base no símbolo digitado |
| `if __name__ == "__main__":` | Ponto de entrada do programa, executado apenas quando o arquivo é rodado diretamente |

---

## ⚠️ Limitações conhecidas

- Não há tratamento de erro para entradas não numéricas (ex.: digitar `"abc"` no lugar de um número causaria um erro de conversão).
- Aceita apenas uma operação por execução — não há suporte a expressões encadeadas (ex.: `2 + 3 * 4`).

---

## 🛠️ Tecnologias utilizadas

- **Python 3** — linguagem de programação

---

## 🎓 Contexto acadêmico

Este projeto foi desenvolvido como atividade prática da disciplina de **Garantia da Qualidade de Software**, com o objetivo de praticar tanto a criação de um algoritmo simples quanto a documentação completa de um projeto seguindo boas práticas de README.

## 👤 Autor

Desenvolvido e documentado por **João Vitor Alves Rodrigues** — RA: 32513480

## 📄 Licença

Este projeto está sob a licença MIT.

# 🎨 Otimização de Compras para Loja de Tintas em Python

Script em Python voltado para a solução de um problema real de logística e consumo de materiais. O programa calcula a quantidade exata de tinta necessária para cobrir uma determinada área em metros quadrados ($\text{m}^2$), aplicando margem de segurança de $10\%$ e otimizando a combinação de embalagens (latas e galões) para atingir o **menor custo financeiro e o menor desperdício de tinta**.

---

## 🎯 Objetivo do Projeto
Oferecer ao cliente três cenários automatizados de compra para pintura residencial ou comercial:
1. **Cenário 1:** Compra exclusiva em latas de 18 Litros.
2. **Cenário 2:** Compra exclusiva em galões de 3,6 Litros.
3. **Cenário 3 (Otimização Efetiva):** Combinação estratégica de latas e galões para mitigar sobras e minimizar o orçamento final.

---

## 🛠️ Tecnologias e Ferramentas
- **Python 3.x**
- **Módulo nativo `math`**
- **VS Code**
- **Git & GitHub**

---

## 💡 Conceitos de Programação Aplicados

- **Operadores Aritméticos Avançados (`//` e `%`):** Uso de divisão inteira para isolar o volume comportado em embalagens de maior capacidade e uso do resto da divisão (*módulo*) para capturar a sobra residual exata de litros.
- **Arredondamento Técnico de Margem (`math.ceil`):** Garantia de que o cliente nunca receba menos tinta do que o estipulado, arredondando qualquer valor fracionado para a unidade inteira superior.
- **Regras de Negócio Dinâmicas:** Cálculo do fator de folga ($10\%$) aplicado diretamente sobre o consumo teórico antes de calcular a distribuição de embalagens.
- **Formatação Monetária (BRL):** Tratamento de saídas numéricas com `f-strings` e conversão de padrão americano (`.`) para o padrão monetário brasileiro (`,`).

---

## 🚀 Como Executar o Projeto

1. Clone o repositório para a sua máquina local:
   ```bash
   git clone https://github.com/PauloWilliamdeFaria/exercicios-python
   ```

2. Acesse a pasta correspondente ao exercício:
   ```bash
   cd exercicios-python/loja_tintas
   ```

3. Execute o script Python:
   ```bash
   python loja_tintas.py
   ```

---

## 💻 Exemplo de Saída no Terminal

```text
============================================================
           LOJA DE TINTAS - OTIMIZAÇÃO DE COMPRA            
============================================================
Digite o tamanho da área a ser pintada (m²): 120

------------------------------------------------------------
Área informada: 120.00 m²
Tinta necessária (com 10% de folga): 22.00 L
------------------------------------------------------------

1) COMPRANDO APENAS LATAS (18L):
   - Quantidade: 2 lata(s)
   - Valor total: R$ 160,00

2) COMPRANDO APENAS GALÕES (3,6L):
   - Quantidade: 7 galão(ões)
   - Valor total: R$ 175,00

3) COMPRA OTIMIZADA (MISTURA DE LATAS E GALÕES):
   - Quantidade: 1 lata(s) e 2 galão(ões)
   - Valor total: R$ 130,00
------------------------------------------------------------
```

---

## 👤 Autor

Desenvolvido por **Paulo William de Faria**.

- **LinkedIn:** [linkedin.com/in/paulowilliamdefaria](https://www.linkedin.com/in/paulowilliamdefaria)
- **GitHub:** [github.com/PauloWilliamdeFaria](https://github.com/PauloWilliamdeFaria)
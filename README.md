# 📊 Análise de Comportamento de Usuários (Funil de Conversão)

## 🎯 Objetivo

Analisar o comportamento de usuários em um ambiente digital, simulando interações reais e identificando padrões de conversão ao longo do funil:

**visita → clique → compra**

A proposta é demonstrar, na prática, habilidades em análise de dados, modelagem e visualização voltadas para contexto de negócio.

---

## 🚀 Tecnologias Utilizadas

* **Python** → geração de dados simulados
* **DuckDB** → processamento e análise com SQL
* **Looker Studio** → construção de dashboard interativo

---

## 🔄 Pipeline do Projeto

O fluxo de dados foi estruturado em três etapas:

1. **Simulação de dados (Python)**

   * Geração de eventos de usuários (visita, clique e compra)
   * Inclusão de variáveis como origem de tráfego e dispositivo

2. **Análise com SQL (DuckDB)**

   * Construção do funil de conversão
   * Cálculo de taxas de conversão
   * Análise por origem de tráfego e device

3. **Visualização (Looker Studio)**

   * Dashboard interativo com KPIs e insights
   * Foco em comunicação clara para tomada de decisão

---

## 📊 Dashboard

🔗 Acesse o dashboard interativo:
https://lookerstudio.google.com/reporting/1751f7f5-855a-4e36-a9f3-6de508dd6164

---

## 📈 Principais Métricas

* **Taxa de conversão total:** ~26%
* **Conversão visita → clique:** ~73%
* **Conversão clique → compra:** ~35%

---

## 🧠 Insights

* A maior perda ocorre na etapa final do funil (**compra**), com aproximadamente **65% de drop-off**
* O canal **Facebook** apresentou a melhor taxa de conversão entre as origens analisadas
* O canal **Instagram** apresentou a menor eficiência de conversão
* A performance entre **mobile** e **desktop** é consistente, indicando experiência semelhante entre dispositivos

---

## 💡 Conclusão

Os dados indicam que o principal ponto de melhoria está na etapa final do processo de conversão, sugerindo possíveis fricções no fluxo de compra (UX, pagamento ou confiança).

A análise também demonstra a importância da avaliação por canal de aquisição para otimização de campanhas.

---

## 📁 Estrutura do Projeto

```
📦 user-behavior-bi
 ┣ 📜 app.py
 ┣ 📜 analise_duckdb.py
 ┣ 📄 eventos_site.csv
 ┣ 📄 funil.csv
 ┣ 📄 conversao_origem.csv
 ┣ 📄 conversao_device.csv
 ┗ 📄 analytics.duckdb
```

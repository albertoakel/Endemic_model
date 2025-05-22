## 🩸 Modelagem de Doenças Endêmicas - Modelos Compartimentais

### 🌐 Visão Geral

Este repositório reúne implementações clássicas e variantes modernas de modelos compartimentais para a modelagem de doenças infecciosas, com foco em contextos endêmicos e cenários aplicados. Os modelos foram implementados em código aberto, com exemplos numéricos e visuais, e visam auxiliar na compreensão, exploração e extensão desses sistemas dinâmicos.

### 🌟 Objetivos

* Reunir implementações dos principais modelos compartimentais (SIR, SEIR, SEIARD etc.)
* Propor adaptações baseadas em dados reais para contextos endêmicos
* Explorar formas de estimação de parâmetros e variáveis
* Servir como base educacional e de experimentação para estudantes e pesquisadores

---

## 📁 Estrutura do Projeto

```bash
modelos-endemicos/
|
├── models/               # Implementação dos modelos matemáticos (ODEs)
│   ├── sir.py            # Modelo SIR
│   ├── seir.py           # Modelo SEIR
│   ├── seiard.py         # Modelo SEIARD
│   └── utils.py          # Funções comuns de integração e plotagem
|
├── notebooks/            # Jupyter Notebooks com exemplos e exploração de dados
│   ├── exemplo_sir.ipynb
│   ├── exemplo_seir.ipynb
│   └── ajuste_dados.ipynb
|
├── data/                 # Dados reais (se aplicável) ou sintéticos para simulação
|
├── sandbox/              # Testes, rascunhos e explorações alternativas
|
├── README.md             # Este documento
└── requirements.txt      # Dependências do projeto
```

---

## 📓 Modelos Compartimentais Implementados

### SIR

* Compartimentos: Suscetíveis, Infectados, Recuperados
* Equações diferenciais de base epidemiológica

### SEIR

* Adição de fase latente (Expostos)
* Útil para doenças com período de incubação

### SEIARD

* Expansão com Assintomáticos e Mortos
* Modelo mais realista para epidemias como a COVID-19

### Estimação de Parâmetros

* Ajuste dos modelos a dados usando métodos de otimização (ex: curva de casos acumulados)

---

## 🔧 Tecnologias e Bibliotecas

* Python 3.x
* NumPy, SciPy, matplotlib, pandas
* Jupyter Notebook
* (Opcional) Streamlit para interfaces interativas

---

## 🌍 Aplicabilidade

Este projeto pode ser usado para:

* Simulação de surtos endêmicos
* Ensino de modelagem matemática em epidemiologia
* Ajuste de modelos a dados reais
* Exploração de cenários com diferentes intervenções

---

## 🙏 Contribuições

Sugestões, melhorias e novos modelos são bem-vindos! Use issues ou pull requests para contribuir.

---

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## 🩸 Modelagem de Doenças Endêmicas - Modelos Compartimentais

### 🌐 Visão Geral

Este repositório reúne implementações clássicas e variantes modernas de modelos compartimentais para a modelagem de
doenças infecciosas, com foco em contextos endêmicos e cenários aplicados. Os modelos foram implementados em 
código aberto, com exemplos numéricos e visuais, e visam auxiliar na compreensão, exploração e extensão
desses sistemas dinâmicos.

### 🌟 Objetivos

* Reunir implementações dos principais modelos compartimentais (SIR, SEIR, SEIARD etc.)
* Propor adaptações baseadas em dados reais para contextos endêmicos
* Explorar formas de estimação de parâmetros e variáveis
* Servir como base educacional e de experimentação para estudantes e pesquisadores

---

## 📁 Estrutura do Projeto

```
Endemic_model/
|
├── model/               # Implementação dos modelos matemáticos (ODEs)
│   ├── modelos_epidemiologicos.py            # Modelos
|
├── notebooks/            # Jupyter Notebooks com exemplos 
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

### Equações diferenciais de base epidemiológica

* SIR
* SEIR
* SEIAR
* SEIARD

### Estimação de Parâmetros

* Ajuste dos modelos a dados usando métodos de otimização 

---

## 🔧 Tecnologias e Bibliotecas

* Python 3.x
* NumPy, SciPy, matplotlib, pandas,lmfit
* Jupyter Notebook
 Streamlit para interfaces interativas (building)

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

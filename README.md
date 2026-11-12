# ✉️ Sistema Inteligente de Triagem de Suporte com IA

Uma aplicação web interativa desenvolvida em **Python** e **Streamlit**, alimentada pela **Google GenAI SDK** (modelo Gemini), criada para automatizar a triagem, categorização e resposta inicial de emails de suporte ao cliente em tempo real.

[![Acessar Aplicação Online](https://img.shields.io/badge/🚀_Testar_App_Online-Streamlit-FF4B4B?style=for-the-badge)](https://sistema-triagem-gemini.streamlit.app)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white)

---

## 🎯 Objetivo do Projeto

O objetivo deste projeto é otimizar o fluxo de trabalho de equipas de atendimento e suporte técnico. Através do processamento de linguagem natural (NLP), a solução analisa automaticamente mensagens recebidas, reduzindo o tempo de resposta e priorizando casos de alta urgência de forma estruturada.

---

## 🚀 Funcionalidades Principais

- **Análise Automática de Urgência e Categoria:** Classifica instantaneamente o email em categorias (ex: *Suporte Técnico*, *Financeiro*, *Comercial*) e define a gravidade (*Baixa*, *Média*, *Alta*).
- **Resumo Técnico Inteligente:** Extrai os pontos críticos do relato do cliente para uma leitura rápida da equipa de atendimento.
- **Minuta de Resposta Empática:** Gera uma proposta de resposta pronta, empática e focada na resolução do problema.
- **Saída Estruturada em JSON:** Força a resposta do modelo no formato JSON estrito, garantindo integridade de dados para integrações via API.
- **Tratamento de Erros e Resiliência:** Conta com lógica de repetição automática (*retry logic*) para lidar com eventuais instabilidades de tráfego na API.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Interface Gráfica:** Streamlit
- **SDK de IA:** `google-genai` (Modelos Gemini 2.5 Flash / 3.8 Flash)
- **Gestão de Ambiente:** `python-dotenv`
- **Controlo de Versão:** Git & GitHub

---

## 📂 Estrutura do Repositório

```text
├── app.py           # Aplicação principal Streamlit e integração com Gemini API
├── .env             # Ficheiro de variáveis de ambiente (Chave de API - não enviado ao Git)
├── .gitignore       # Proteção de ficheiros sensíveis e temporários
└── README.md        # Documentação completa do projeto

```

## Como Executar o Projeto

1. **Clona o repositório:**
   ```bash
   git clone [https://github.com/felipe2008jmf-mec/processador-relatorios-gemini.git](https://github.com/felipe2008jmf-mec/processador-relatorios-gemini.git)
   cd processador-relatorios-gemini


2. **Instale as depêndencias**
   ```bash
   pip install streamlit google-genai python-dotenv

3. Configure sua chave API:
   ```bash
   Cria um ficheiro chamado .env na raiz do projeto e adiciona a tua chave da API da seguinte forma: GEMINI_API_KEY=suachaveaqui

5. Execute o código
   ```bash
   streamlit run app.py


<img width="1062" height="920" alt="Captura de tela 2026-11-03 214107" src="https://github.com/user-attachments/assets/b515bf81-d138-422a-abd1-b106c0707b82" />



## AUTOR: Felipe Freitas

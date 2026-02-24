# 🤖 Customer Service AI Agent

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-Vertex_AI-4285F4.svg)
![Generative AI](https://img.shields.io/badge/Generative_AI-Gemini-8E75B2.svg)

## 📌 Sobre o Projeto

Este projeto implementa um **Agente de Inteligência Artificial** focado em Atendimento ao Cliente (Customer Service), desenvolvido com a stack do Google Cloud e modelos generativos. 

O agente é capaz de interpretar requisições em linguagem natural, analisar o contexto e tomar decisões automatizadas utilizando *Function Calling* (chamada de ferramentas), como verificar o conteúdo de devoluções de produtos, identificar divergências e alertar sobre possíveis fraudes estruturadas.

## 🏗️ Arquitetura e Tecnologias

A arquitetura foi desenhada para ser escalável e testável, incorporando práticas modernas de engenharia de software e IA:

* **Linguagem:** Python
* **IA Generativa:** Google Vertex AI (Modelos Gemini)
* **Avaliação de Agentes (Eval):** Framework de testes automatizados para validar a precisão e a segurança das respostas do agente (`adk_eval`).
* **Integração e Orquestração:** Gestão de estado e contexto de conversas utilizando ferramentas personalizadas.

## ⚙️ Funcionalidades Principais

* **Processamento de Linguagem Natural:** Entendimento de intenções e extração de entidades de mensagens de clientes.
* **Validação de Devoluções (`verify_return_contents`):** Comparação automatizada entre itens esperados e itens recebidos.
* **Deteção de Anomalias:** Avaliação de risco e acionamento de alertas de fraude (`fraud_alert_level`).

---

## 🚀 Como Executar e Avaliar (Running Evaluations)

This directory contains the customer service agent and its evaluation tests. There are several ways to run evaluations:

### 1. Recommended: Programmatic Evaluation (Pytest)

This method is more robust and avoids naming conflicts with the ADK CLI.

**From the project root directory (`adk_eval/`):**
```bash
PYTHONPATH=. uv run pytest customer_service_agent/test_agent_eval.py

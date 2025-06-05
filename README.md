# 🍕 Charles Pizzas Congeladas

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Branch](https://img.shields.io/badge/branch-integrando--o--back--end-blue)](https://github.com/ajudantedemagico/charlespizzascongeladas/tree/integrando-o-back-end)

Sistema de gerenciamento para pizzaria desenvolvido como projeto acadêmico.

## 📌 Sumário
- [Funcionalidades]
- [Tecnologias]
- [Pré-requisitos]
- [Instalação]
- [Configuração]
- [Estrutura-do-Projeto]
- [API]
- [Contribuição]
- [Licença]
- [Autores]

# ✨ Funcionalidades
- Catálogo de pizzas congeladas
- Sistema de pedidos
- Gerenciamento de estoque
- Autenticação de usuários
- Relatórios de vendas

# 💻 Tecnologias
**Front-end:**
- HTML
- CSS
- JavaScript
- Figma

**Back-end:**
- Python
- JSON
- MVC

**Ferramentas:**
- Git
- GitHub
- Visual Studio Code
- WhatsApp

**Banco De Dados**
- MySQL

**Engenharia de Software**
- plantUML

## 📋 Pré-requisitos
- requirements.txt

## 🛠️ Instalação

# Clone o repositório
git clone -b integrando-o-back-end https://github.com/ajudantedemagico/charlespizzascongeladas.git

# Crie o ambiente virtual
python -m venv venv 

# Ative o ambiente virtual
.\venv\Scripts\activate

# Instale os pacotes necessários
pip install -r requirements.txt 
pip install "fastapi[standard]" 
pip install mysql-connector-python 
pip install itsdangerous

# Inicialize o sistema
python main.py

## ⚙️ Configuração

# Configure suas credenciais do MySQL:
DB_HOST= localhost
DB_USER= root
DB_PASSWORD= root
DB_NAME= charles_pizzaria

## 📂 Estrutura do Projeto

charlespizzascongeladas/
├── backend/           # API
│   ├── controllers/   # Lógica das rotas
│   ├── database/      # Configuração Banco de Dados
│   ├── models/        # Modelos
│   ├── routes/        # Definição de rotas
├── frontend/          
│   ├── static/
│   │   ├── CSS/
│   │   ├── img/
│   │   ├── JS/
│   ├── templates/
│   │   ├── HTML
├── .gitignore
└── README.md

## 🌐 API

Endpoints principais:

GET /pizzas - Lista todas as pizzas

POST /pedidos - Cria novo pedido

GET /estoque - Verifica disponibilidade

## 🤝 Contribuição

Faça um fork do projeto

Crie uma branch: git checkout -b minha-feature

Commit suas mudanças: git commit -m 'feat: Minha nova feature'

Push para a branch: git push origin minha-feature

Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo LICENSE para detalhes.

## 👥 Autores

github.com/Arthuranjo
github.com/caiodevjr
github.com/ajudantedemagico
github.com/Juhh006
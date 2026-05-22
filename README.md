# Loan Management System

Sistema de empréstimo de livros desenvolvido como projeto de estudo para backend e gerenciamento de dados.

## 🚀 Descrição
Este projeto simula um sistema de controle de empréstimos de livros, com funções de cadastro, consulta e devolução de itens. Ele é ideal para aprender conceitos de API, persistência de dados e arquitetura de aplicação em Python.

## ✅ Funcionalidades
- Cadastro e listagem de livros
- Cadastro e listagem de usuários
- Registro de empréstimos de livros
- Controle de devoluções
- Consulta de histórico e status de empréstimos

## 🛠️ Tecnologias
- Python
- Flask
- SQL (SQLite ou similar)
- Git/GitHub

## 📁 Estrutura do projeto
- `main.py` — ponto de entrada da aplicação
- `database/connection.py` — configuração da conexão com o banco
- `database/setup.py` — inicialização/estrutura do banco de dados
- `models/` — classes e modelos de dados
  - `livro.py`
  - `usuario.py`
  - `emprestimo.py`
- `routes/` — rotas da API
  - `livros.py`
  - `usuarios.py`
  - `emprestimos.py`

## ▶️ Como executar
1. Crie um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   ```
2. Ative o ambiente virtual:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute a aplicação:
   ```bash
   python main.py
   ```

## 🧪 Uso
Após iniciar a aplicação, acesse as rotas definidas em `routes/` para gerenciar livros, usuários e empréstimos. Por exemplo:
- `GET /livros`
- `POST /usuarios`
- `POST /emprestimos`
- `PUT /emprestimos/<id>/devolver`

## 🎯 Objetivos do projeto
- Praticar desenvolvimento backend com Python e Flask
- Estruturar rotas e endpoints REST
- Trabalhar com persistência de dados em banco
- Organizar código por camadas e responsabilidades

## 📚 Aprendizados
Principais temas estudados e aplicados:
- Desenvolvimento de API REST
- Organização de projeto Python
- Programação orientada a objetos
- Modelagem de dados e controle de empréstimos
- Organização de rotas e estruturas de arquivos

## 📌 Observações
- Ideal para usar como base em projetos de estudo ou portfólio
- Pode ser expandido com autenticação, frontend e testes automatizados

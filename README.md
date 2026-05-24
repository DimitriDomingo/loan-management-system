# Sistema de Empréstimo de Livros

API backend desenvolvida com Python e Flask para gerenciamento de livros, usuários e empréstimos.

O projeto possui arquitetura em camadas utilizando:
- Routes
- Services
- Repository

Além disso, utiliza banco de dados relacional SQLite com:
- Foreign Keys
- JOINs
- Regras de negócio
- Controle de estoque

---

# Tecnologias Utilizadas

- Python
- Flask
- SQLite
- SQL
- Git/GitHub

---

# Funcionalidades

## Livros
- Cadastrar livros
- Listar livros
- Atualizar livros
- Deletar livros

## Usuários
- Cadastrar usuários
- Listar usuários
- Atualizar usuários
- Deletar usuários

## Empréstimos
- Realizar empréstimos
- Listar empréstimos
- Devolver livros
- Controle automático de estoque

---

# Estrutura do Projeto

```text
project/
│
├── database/
│   ├── connection.py
│   └── setup.py
│
├── models/
│
├── repositories/
│   ├── livro_repository.py
│   ├── usuario_repository.py
│   └── emprestimo_repository.py
│
├── routes/
│   ├── livros.py
│   ├── usuarios.py
│   └── emprestimos.py
│
├── services/
│   ├── livro_service.py
│   ├── usuario_service.py
│   └── emprestimo_service.py
│
├── app.py
└── requirements.txt
```

---

# Arquitetura

## Routes
Responsáveis por:
- receber requisições HTTP
- retornar respostas
- definir status HTTP

---

## Services
Responsáveis por:
- regras de negócio
- validações
- controle do fluxo da aplicação

---

## Repository
Responsáveis por:
- acesso ao banco de dados
- execução de SQL
- manipulação de consultas

---

# Banco de Dados

O projeto utiliza SQLite com relacionamento entre tabelas utilizando Foreign Keys.

Exemplo:
- empréstimos relacionados a usuários
- empréstimos relacionados a livros

Também são utilizados JOINs para retornar informações completas nas consultas.

---

# Como Executar o Projeto

## 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

---

## 2. Entrar na pasta

```bash
cd nome-do-projeto
```

---

## 3. Criar ambiente virtual

```bash
python -m venv venv
```

---

## 4. Ativar ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 5. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 6. Executar aplicação

```bash
python app.py
```

---

# Endpoints

## Livros

| Método | Endpoint | Descrição |
|---|---|---|
| GET | /livros | Listar livros |
| POST | /livros | Criar livro |
| PUT | /livros/id | Atualizar livro |
| DELETE | /livros/id | Deletar livro |

---

## Usuários

| Método | Endpoint | Descrição |
|---|---|---|
| GET | /usuarios | Listar usuários |
| POST | /usuarios | Criar usuário |
| PUT | /usuarios/id | Atualizar usuário |
| DELETE | /usuarios/id | Deletar usuário |

---

## Empréstimos

| Método | Endpoint | Descrição |
|---|---|---|
| GET | /emprestimos | Listar empréstimos |
| POST | /emprestimos | Realizar empréstimo |
| PUT | /emprestimos/id | Devolver livro |

---

# Regras de Negócio

- Não é possível emprestar livro sem estoque
- Não é possível devolver livro já devolvido
- O estoque é atualizado automaticamente
- Usuários e livros precisam existir para realizar empréstimos

---

# Objetivo do Projeto

O projeto foi desenvolvido com foco em:
- aprendizado de backend
- arquitetura em camadas
- APIs REST
- integração com banco de dados relacional
- boas práticas de organização backend
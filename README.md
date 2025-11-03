# 🚗 Sistema de Frotas - Fleet Management System

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey.svg)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Sistema web completo de autenticação e gerenciamento construído com Flask, focado em segurança e escalabilidade. Ideal como base para sistemas de gestão de frotas, logística e mobilidade.

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Uso](#-uso)
- [Endpoints da API](#-endpoints-da-api)
- [Segurança](#-segurança)
- [Screenshots](#-screenshots)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)
- [Contato](#-contato)

---

## 🎯 Visão Geral

O **Sistema de Frotas** é uma aplicação web desenvolvida em Flask que oferece um sistema robusto de autenticação de usuários com foco em segurança e boas práticas de desenvolvimento. O projeto utiliza arquitetura modular, facilitando a extensão para funcionalidades mais complexas como dashboards administrativos, APIs RESTful e integração com sistemas de gestão de frotas.

### Por que usar este sistema?

- ✅ **Segurança em primeiro lugar**: Senhas hasheadas com Werkzeug
- ✅ **Arquitetura modular**: Fácil de estender e manter
- ✅ **Pronto para produção**: Estrutura escalável para aplicações reais
- ✅ **Documentação completa**: Tutorial passo a passo incluído

---

## ⚡ Funcionalidades

### Autenticação
- 🔐 **Registro de Usuários**: Cadastro com validação de email e username únicos
- 🔑 **Login Seguro**: Autenticação com verificação de credenciais hasheadas
- 🚪 **Logout**: Gerenciamento seguro de sessões
- 🛡️ **Proteção de Rotas**: Páginas restritas acessíveis apenas após autenticação

### Segurança
- 🔒 Hash de senhas com Werkzeug
- 🍪 Gerenciamento de sessões com Flask-Login
- 🔐 Proteção CSRF
- 🚫 Validação de dados de entrada

---

## 🛠️ Tecnologias

| Tecnologia | Versão | Descrição |
|-----------|--------|-----------|
| **Python** | 3.x | Linguagem principal |
| **Flask** | 2.x | Framework web |
| **Flask-Login** | - | Gerenciamento de sessões |
| **Werkzeug** | - | Segurança e hash de senhas |
| **SQLite** | 3 | Banco de dados (desenvolvimento) |
| **Jinja2** | - | Template engine |
| **HTML/CSS** | 5/3 | Frontend |

---

## 📁 Estrutura do Projeto

```
sistema-frotas/
│
├── app/                          # Diretório principal da aplicação
│   ├── __init__.py              # Inicialização do app Flask
│   ├── models.py                # Modelos de dados (User, etc.)
│   ├── routes.py                # Definição de rotas e endpoints
│   ├── forms.py                 # Formulários WTForms
│   ├── auth.py                  # Lógica de autenticação
│   │
│   ├── templates/               # Templates HTML (Jinja2)
│   │   ├── base.html           # Template base
│   │   ├── index.html          # Página inicial
│   │   ├── register.html       # Página de cadastro
│   │   ├── login.html          # Página de login
│   │   └── dashboard.html      # Dashboard (protegido)
│   │
│   └── static/                  # Arquivos estáticos
│       ├── css/                # Estilos CSS
│       ├── js/                 # Scripts JavaScript
│       └── img/                # Imagens
│
├── screenshots/                 # Capturas de tela do sistema
│   ├── home.png
│   ├── register.png
│   └── login.png
│
├── __pycache__/                # Cache Python (ignorado no git)
│
├── run.py                      # Script principal para executar o app
├── requirements.txt            # Dependências do projeto
├── .gitignore                  # Arquivos ignorados pelo Git
└── README.md                   # Este arquivo

```

### Descrição dos Diretórios

#### 📂 `/app`
Contém toda a lógica da aplicação:
- **`__init__.py`**: Factory function para criar a instância do Flask
- **`models.py`**: Definição dos modelos de banco de dados (SQLAlchemy)
- **`routes.py`**: Todas as rotas HTTP da aplicação
- **`auth.py`**: Funções de autenticação e autorização
- **`forms.py`**: Formulários com validação (WTForms)

#### 📂 `/app/templates`
Templates HTML renderizados pelo Jinja2:
- **`base.html`**: Template base com navbar e footer
- **`index.html`**: Página inicial pública
- **`register.html`**: Formulário de cadastro
- **`login.html`**: Formulário de login
- **`dashboard.html`**: Área restrita do usuário

#### 📂 `/app/static`
Recursos estáticos (CSS, JS, imagens)

#### 📂 `/screenshots`
Imagens de demonstração do sistema

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)
- virtualenv (recomendado)

### Passo a Passo

#### 1. Clone o repositório

```bash
git clone https://github.com/rdralves/sistema-frotas.git
cd sistema-frotas
```

#### 2. Crie um ambiente virtual

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

#### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

#### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua_chave_secreta_super_segura_aqui
FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=sqlite:///database.db
```

#### 5. Inicialize o banco de dados

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

---

## ⚙️ Configuração

### Configuração do Banco de Dados

Por padrão, o sistema usa SQLite para desenvolvimento. Para produção, recomenda-se PostgreSQL ou MySQL.

**Exemplo de configuração PostgreSQL:**

```python
# app/__init__.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/dbname'
```

### Configuração de Segurança

Edite `app/__init__.py` para configurar:

```python
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'chave-super-secreta'
app.config['SESSION_COOKIE_SECURE'] = True  # Apenas HTTPS
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
```

---

## 💻 Uso

### Executando o Servidor de Desenvolvimento

```bash
python run.py
```

O servidor estará disponível em: **http://localhost:5000**

### Acessando o Sistema

1. **Página Inicial**: http://localhost:5000/
2. **Cadastro**: http://localhost:5000/register
3. **Login**: http://localhost:5000/login
4. **Dashboard**: http://localhost:5000/dashboard (requer login)

### Criando o Primeiro Usuário

1. Acesse `/register`
2. Preencha o formulário:
   - Nome completo
   - Email (único)
   - Username (único)
   - Senha (mínimo 6 caracteres)
3. Clique em "Cadastrar"
4. Faça login com suas credenciais

---

## 🔌 Endpoints da API

### Autenticação

#### `GET /`
**Descrição**: Página inicial pública  
**Autenticação**: Não requerida  
**Resposta**: Renderiza `index.html`

```http
GET / HTTP/1.1
Host: localhost:5000
```

---

#### `GET /register`
**Descrição**: Exibe formulário de cadastro  
**Autenticação**: Não requerida  
**Resposta**: Renderiza `register.html`

```http
GET /register HTTP/1.1
Host: localhost:5000
```

---

#### `POST /register`
**Descrição**: Processa cadastro de novo usuário  
**Autenticação**: Não requerida  
**Content-Type**: `application/x-www-form-urlencoded`

**Parâmetros do Formulário:**

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `name` | string | Sim | Nome completo do usuário |
| `email` | string | Sim | Email único (validado) |
| `username` | string | Sim | Username único |
| `password` | string | Sim | Senha (mínimo 6 caracteres) |

**Exemplo de Requisição:**

```http
POST /register HTTP/1.1
Host: localhost:5000
Content-Type: application/x-www-form-urlencoded

name=João+Silva&email=joao@example.com&username=joaosilva&password=senha123
```

**Respostas:**

- **201 Created**: Usuário criado com sucesso (redirect para `/login`)
- **400 Bad Request**: Dados inválidos ou email/username já existente
- **500 Internal Server Error**: Erro no servidor

---

#### `GET /login`
**Descrição**: Exibe formulário de login  
**Autenticação**: Não requerida  
**Resposta**: Renderiza `login.html`

```http
GET /login HTTP/1.1
Host: localhost:5000
```

---

#### `POST /login`
**Descrição**: Autentica usuário e cria sessão  
**Autenticação**: Não requerida  
**Content-Type**: `application/x-www-form-urlencoded`

**Parâmetros do Formulário:**

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `username` | string | Sim | Username ou email |
| `password` | string | Sim | Senha do usuário |
| `remember` | boolean | Não | Manter conectado |

**Exemplo de Requisição:**

```http
POST /login HTTP/1.1
Host: localhost:5000
Content-Type: application/x-www-form-urlencoded

username=joaosilva&password=senha123&remember=on
```

**Respostas:**

- **200 OK**: Login bem-sucedido (redirect para `/dashboard`)
- **401 Unauthorized**: Credenciais inválidas
- **500 Internal Server Error**: Erro no servidor

---

#### `GET /logout`
**Descrição**: Encerra sessão do usuário  
**Autenticação**: Requerida  
**Resposta**: Redirect para página inicial

```http
GET /logout HTTP/1.1
Host: localhost:5000
Cookie: session=abc123...
```

**Respostas:**

- **302 Found**: Logout bem-sucedido (redirect para `/`)
- **401 Unauthorized**: Usuário não autenticado

---

### Rotas Protegidas

#### `GET /dashboard`
**Descrição**: Dashboard do usuário autenticado  
**Autenticação**: Requerida (Flask-Login)  
**Resposta**: Renderiza `dashboard.html`

```http
GET /dashboard HTTP/1.1
Host: localhost:5000
Cookie: session=abc123...
```

**Respostas:**

- **200 OK**: Dashboard renderizado
- **302 Found**: Redirect para `/login` (não autenticado)

---

### Códigos de Status HTTP

| Código | Descrição |
|--------|-----------|
| 200 | Requisição bem-sucedida |
| 201 | Recurso criado com sucesso |
| 302 | Redirecionamento |
| 400 | Requisição inválida |
| 401 | Não autenticado |
| 403 | Acesso negado |
| 404 | Recurso não encontrado |
| 500 | Erro interno do servidor |

---

## 🔒 Segurança

### Boas Práticas Implementadas

1. **Hash de Senhas**: Utiliza `werkzeug.security` para hash bcrypt
2. **Proteção CSRF**: Tokens CSRF em todos os formulários
3. **Validação de Entrada**: Sanitização de dados com WTForms
4. **Sessões Seguras**: Cookies HttpOnly e Secure
5. **SQL Injection**: Prevenção via SQLAlchemy ORM

### Recomendações para Produção

```python
# Configurações de segurança para produção
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    PERMANENT_SESSION_LIFETIME=timedelta(hours=1)
)
```

---

## 📸 Screenshots

### Página Inicial
![Home](screenshots/home.png)

### Tela de Cadastro
![Register](screenshots/register.png)

### Tela de Login
![Login](screenshots/login.png)

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga os passos abaixo:

1. **Fork** o projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/MinhaFeature`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. **Push** para a branch (`git push origin feature/MinhaFeature`)
5. Abra um **Pull Request**

### Diretrizes

- Siga o padrão PEP 8 para código Python
- Adicione testes para novas funcionalidades
- Atualize a documentação conforme necessário
- Mantenha commits atômicos e descritivos


## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📧 Contato

**Rodrigo Alves**

- 🔗 LinkedIn: [linkedin.com/in/rodrigoalvesreis](https://www.linkedin.com/in/rodrigoalvesreis/)
- 📧 Email: rdr.alves@gmail.com
- 🐙 GitHub: [@rdralves](https://github.com/rdralves)

---

## documentação

- [Flask](https://flask.palletsprojects.com/) - Framework web
- [Flask-Login](https://flask-login.readthedocs.io/) - Gerenciamento de sessões
- [Werkzeug](https://werkzeug.palletsprojects.com/) - Utilitários WSGI
- Comunidade Python Brasil

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela!**

Desenvolvido com ❤️ por [Rodrigo Alves](https://github.com/rdralves)

</div>
